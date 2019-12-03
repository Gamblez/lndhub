import os
# import pytest

from lndhub.models import Wallet


TEST_WALLETS = os.environ['TEST_WALLETS'].split(' ')


class TestLndHub:

    def test_decode_invoice(self):
        wallet = Wallet(TEST_WALLETS[0])
        assert wallet.decode_invoice('lnbc20m1pvjluezhp58yjmdan79s6qqdhdzgynm4zwqd5d7xmw5fk98klysy043l2ahrqspp5qqqsyqcyq5rqwzqfqqqsyqcyq5rqwzqfqqqsyqcyq5rqwzqfqypqfppqw508d6qejxtdg4y5r3zarvary0c5xw7kepvrhrm9s57hejg0p662ur5j5cr03890fa7k2pypgttmh4897d3raaq85a293e9jpuqwl0rnfuwzam7yr8e690nd2ypcq9hlkdwdvycqa0qza8')['num_satoshis'] == '2000000'
