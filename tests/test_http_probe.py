from __future__ import annotations

import unittest
from datetime import timedelta

from scripts.http_probe import probe_url


class FakeResponse:
    url = "https://example.com/final"
    status_code = 200
    elapsed = timedelta(milliseconds=125)
    content = b"hello"


class FakeClient:
    def __init__(self) -> None:
        self.request: tuple[str, float, bool] | None = None

    def get(self, url: str, *, timeout: float, allow_redirects: bool):
        self.request = (url, timeout, allow_redirects)
        return FakeResponse()


class ProbeUrlTests(unittest.TestCase):
    def test_returns_response_metadata(self) -> None:
        client = FakeClient()

        result = probe_url(
            "https://example.com",
            timeout=3.5,
            client=client,
        )

        self.assertEqual(
            client.request,
            ("https://example.com", 3.5, True),
        )
        self.assertEqual(result.url, "https://example.com/final")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.elapsed_seconds, 0.125)
        self.assertEqual(result.content_length, 5)


if __name__ == "__main__":
    unittest.main()
