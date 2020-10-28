import requests

from typing import List, Optional, Tuple

from .exceptions import InvalidLndHubUrl, LndRouteNotFoundException, raise_for_code


class Invoice:
    """
    https://github.com/BlueWallet/LndHub/blob/master/doc/Send-requirements.md
    """


class Transaction:
    """
    https://github.com/BlueWallet/LndHub/blob/master/doc/Send-requirements.md
    ---
    {
        "type": "...", // string, type of txs. Types:
            // bitcoind_internal_tx   - moves to user btc address or account
            // bitcoind_tx   - received by address or account
            // paid_invoice  - user paid someone's invoice
            // sent_coins - user sent coins by lnd to someone's btc account
            // received_invoice_payments - user received payments by invoice
        "txid": "...", // string, internal tx id. not related to onchain transaction id
        "amt": 666, // satoshi, int
        "fee": 11, // satoshi, int
        "timestamp": 1234567, // int, unixtime
        "from": "...", // string
        "to": "...", // string
        "description": "...", // string, user-defined text
        "invoice": "...", // string, original bolt11-format invoice
    }
    """


class LndHub:
    DEFAULT_ENDPOINT = 'https://lndhub.herokuapp.com/'

    def __init__(self, url: str) -> None:
        self.url = url
        if not url.startswith('lndhub://') or not self.endpoint.startswith('https://'):
            raise InvalidLndHubUrl

    def __str__(self) -> str:
        return self.url

    @property
    def endpoint(self) -> str:
        if '@' in self.url:
            endpoint = self.url.split('@')[1]
            return endpoint if endpoint.endswith('/') else endpoint + '/'
        return self.DEFAULT_ENDPOINT

    @property
    def credentials(self) -> Tuple[str, str]:
        return tuple(self.url.replace('lndhub://', '').split('@')[0].split(':'))


class Wallet:
    access_token: str = None
    refresh_token: str = None

    def __init__(self, lndhub: str) -> None:
        self.lndhub = LndHub(lndhub)
        self.authenticate()

    def __str__(self) -> str:
        return self.lndhub.url

    def _process_response(self, res: dict) -> dict:
        """Check for NotFound errors, LndHub errors, etc. If no errors are found, return parsed JSON."""
        if res.status_code == 404:
            raise LndRouteNotFoundException

        res = res.json()
        if 'error' in res and res['error']:
            raise_for_code(res['code'], message=res['message'])

        return res

    def _get(self, endpoint: str, *, data: dict = {}) -> dict:
        with requests.Session() as s:
            headers = {'Authorization': 'Bearer ' + self.access_token}
            res = s.get(self.lndhub.endpoint + endpoint, params=data, headers=headers)
        return self._process_response(res)

    def _post(self, endpoint: str, *, data: dict = {}, bearer_auth: bool = True) -> dict:
        with requests.Session() as s:
            headers = {'Authorization': 'Bearer ' + self.access_token} if bearer_auth else {}
            res = s.post(self.lndhub.endpoint + endpoint, json=data, headers=headers)
        return self._process_response(res)

    def authenticate(self) -> None:
        login, password = self.lndhub.credentials
        res = self._post('auth?type=auth', data={'login': login, 'password': password}, bearer_auth=False)
        self.access_token, self.refresh_token = res['access_token'], res['refresh_token']

    def get_info(self):
        return self._get('getinfo')

    def get_balance(self):
        return self._get('balance')

    def get_transactions(self, limit: int = 20, *, offset: int = 0) -> List[Transaction]:
        """TODO: Transaction typing."""
        return [tx for tx in self._get('gettxs', data={'limit': limit, 'offset': offset})]

    def get_transaction(self, txid: int) -> Transaction:
        """TODO: Transaction typing."""
        return self._get('gettx', data={'txid': txid})

    def get_pending_transactions(self) -> List[Transaction]:
        """TODO: Transaction typing."""
        return [tx for tx in self._get('getpending')]

    def get_invoices(self) -> List[Invoice]:
        """TODO: Invoice typing."""
        return [inv for inv in self._get('getuserinvoices')]

    def create_invoice(self, amount: int, description: str = '') -> Optional[Invoice]:
        """TODO: Invoice typing."""
        return self._post('addinvoice', data={'amt': amount, 'memo': description})

    def decode_invoice(self, bolt11_invoice: str) -> Invoice:
        """TODO: Invoice typing."""
        return self._get('decodeinvoice', data={'invoice': bolt11_invoice})

    def check_invoice_route(self, bolt11_invoice: str):
        raise NotImplementedError

    def pay_invoice(self, bolt11_invoice: str):
        raise NotImplementedError

    def get_btc_addresses(self) -> List[str]:
        return [btc['address'] for btc in self._get('getbtc')]

    def create_btc_address(self) -> str:
        return self._get('newbtc')['address']
