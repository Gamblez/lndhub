LndHub
======

[![travis-badge]][travis]
[![codecov-badge]][codecov]
[![pypi-badge]][pypi]
[![license-badge]](LICENSE)

With `lndhub` you can interact with wallets that provide a LndHub URL like BlueWallet or lntxbot.

This library is still in pre-alpha and it can change a lot. The idea is to be able to interact
with all API endpoints defined in the [`BlueWallet/LndHub` documentation][lndhub-docs]:

- [ ] `...`: `/create`
- [ ] `...`: `/oauth2/token`
- [x] `Wallet.authenticate()`: `/auth`
- [x] `Wallet.get_info()`: `/getinfo`
- [x] `Wallet.get_balance()`: `/balance`
- [x] `Wallet.get_transactions()`: `/gettxs`
- [x] `Wallet.get_transaction(id)`: `/gettx`
- [x] `Wallet.get_pending_transactions()`: `/getpending`
- [x] `Wallet.get_invoices()`: `/getuserinvoices`
- [x] `Wallet.create_invoice(amount, description)`: `/addinvoice`
- [x] `Wallet.decode_invoice(bolt11)`: `/decodeinvoice`
- [ ] `...`: `/checkrouteinvoice` at the momment [does nothing][lndhub-checkrouteinvoice].
- [ ] `Wallet.pay_invoice(bolt11)`: `/payinvoice`
- [ ] `...`: `/sendcoins`
- [x] `Wallet.get_btc_addresses()`: `/getbtc`
- [x] `Wallet.create_btc_address()`: `/newbtc`

Basic usage
-----------

```python
import os

from lndhub import Wallet

wallet = Wallet(os.environ['LNDHUB_WALLET'])  # lndhub://user:pass@https://endpoint.com
balance = wallet.get_balance()
invoice = wallet.create_invoice(amount=200, description='Thanks!')
```

[travis-badge]: https://travis-ci.org/eillarra/lndhub.svg?branch=master
[travis]: https://travis-ci.org/eillarra/lndhub?branch=master
[codecov-badge]: https://codecov.io/gh/eillarra/lndhub/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/eillarra/lndhub
[pypi-badge]: https://badge.fury.io/py/lndhub.svg
[pypi]: https://pypi.org/project/lndhub/
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg

[lndhub-docs]: https://github.com/BlueWallet/LndHub/blob/master/doc/Send-requirements.md
[lndhub-checkrouteinvoice]: https://github.com/BlueWallet/LndHub/blob/master/controllers/api.js#L363
