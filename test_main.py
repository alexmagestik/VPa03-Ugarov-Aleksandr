import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest import mock

import main


class TestMain(unittest.TestCase):
    @mock.patch("main.requests.get")
    def test_fetch_uses_given_url(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"content"

        r = main.fetch("https://example.com")

        mock_get.assert_called_once_with("https://example.com")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b"content")

    @mock.patch("main.requests.get")
    def test_main_uses_argv_url(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"content"

        buffer = io.StringIO()

        with mock.patch.object(sys, "argv", ["main.py", "https://argv.com"]), redirect_stdout(buffer):
            main.main()

        mock_get.assert_called_once_with("https://argv.com")
        self.assertIn("200", buffer.getvalue())

    @mock.patch("main.requests.get")
    def test_main_uses_default_url_without_args(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"content"

        buffer = io.StringIO()

        with mock.patch.object(sys, "argv", ["main.py"]), redirect_stdout(buffer):
            main.main()

        mock_get.assert_called_once_with("https://something.com")


if __name__ == "__main__":
    unittest.main()