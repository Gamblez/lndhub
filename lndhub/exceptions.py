class LndHubException(Exception):
    pass


class InvalidLndHubUrl(LndHubException, ValueError):
    """The LndHub URL provided was somehow invalid."""


class BadAuthException(LndHubException):
    """Bad auth."""


class NotEnoughBalanceException(LndHubException):
    """Not enough balance."""


class BadPartnerException(LndHubException):
    """Bad partner."""


class NotValidInvoiceException(LndHubException):
    """Not a valid invoice."""


class LndRouteNotFoundException(LndHubException):
    """LND route not found."""


class ServerErrorException(LndHubException):
    """General server error."""


class LndFailureException(LndHubException):
    """LND failure."""


def raise_for_code(code: int, *, message: str = '') -> None:
    raise {
        1: BadAuthException,
        2: NotEnoughBalanceException,
        3: BadPartnerException,
        4: NotValidInvoiceException,
        5: LndRouteNotFoundException,
        6: ServerErrorException,
        7: LndFailureException,
    }[code](message)
