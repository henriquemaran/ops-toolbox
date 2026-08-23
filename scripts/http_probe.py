"""Probe an HTTP endpoint without printing or storing its response body."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Protocol

import requests


class HttpClient(Protocol):
    """Subset of the requests API used by this module."""

    def get(self, url: str, *, timeout: float, allow_redirects: bool): ...


@dataclass(frozen=True)
class ProbeResult:
    url: str
    status_code: int
    elapsed_seconds: float
    content_length: int


def probe_url(
    url: str,
    *,
    timeout: float = 10.0,
    client: HttpClient = requests,
) -> ProbeResult:
    """Return basic response metadata for *url*.

    The response body is used only to calculate its size and is never printed.
    """

    response = client.get(url, timeout=timeout, allow_redirects=True)
    return ProbeResult(
        url=response.url,
        status_code=response.status_code,
        elapsed_seconds=response.elapsed.total_seconds(),
        content_length=len(response.content),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="HTTP or HTTPS URL to probe")
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="request timeout in seconds (default: 10)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        result = probe_url(args.url, timeout=args.timeout)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return 2

    print(f"URL: {result.url}")
    print(f"Status: {result.status_code}")
    print(f"Elapsed: {result.elapsed_seconds:.3f}s")
    print(f"Body size: {result.content_length} bytes")
    return 0 if 200 <= result.status_code < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main())
