from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO

import sys


class TestUrlPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'google'
        domain = 'com'
        expected_url = f'{protocol}://{host}.{domain}'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            url_print(protocol, host, domain)
            self.assertTrue(expected_url in fake_out.getvalue())

        # with self.assertWarns(Warning)
        # with self.assertRaises(TypeError)


def url_print(protocol, host, domain):
    url = f'{protocol}://{host}.{domain}'
    print(url, file=sys.stdout)


if __name__ == '__main__':
    main()
