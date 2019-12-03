import pytest

from lndhub.exceptions import InvalidLndHubUrl
from lndhub.models import LndHub


class TestLndHub:

    @pytest.mark.parametrize('url', [
        'fc3645b439ce8e7f2553a69:e5267081d96dcd340693afabe0',
        'lndhub://fc3645b439ce8e7f2553a69:e5267081d96dcd340693afabe0@http://lndhub.herokuapp.com',
        'lndhub://fc3645b439ce8e7f2553a69:e5267081d96dcd340693afabe0@lndhub.herokuapp.com',
    ])
    def test_invalid(self, url):
        with pytest.raises(InvalidLndHubUrl):
            LndHub(url)

    @pytest.mark.parametrize('url', [
        'lndhub://fc3645b439ce8e7f2553a69:e5267081d96dcd340693afabe0',
        'lndhub://fc3645b439ce8e7f2553a69:e5267081d96dcd340693afabe0@https://lndhub.herokuapp.com',
    ])
    def test_valid(self, url):
        lnurl = LndHub(url)
        assert str(lnurl) == url
        assert lnurl.credentials == ('fc3645b439ce8e7f2553a69', 'e5267081d96dcd340693afabe0')
        assert lnurl.endpoint == 'https://lndhub.herokuapp.com/'
