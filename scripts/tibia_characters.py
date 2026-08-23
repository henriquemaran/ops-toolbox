"""List the other characters returned by the public TibiaData API."""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from typing import Protocol
from urllib.parse import quote

import requests


API_BASE_URL = "https://api.tibiadata.com/v4/character"


class HttpClient(Protocol):
    """Subset of the requests API used by this module."""

    def get(self, url: str, *, headers: dict[str, str], timeout: float): ...


@dataclass(frozen=True)
class Character:
    name: str
    status: str


def fetch_other_characters(
    character_name: str,
    *,
    timeout: float = 10.0,
    client: HttpClient = requests,
) -> list[Character]:
    """Fetch the characters associated with a Tibia character."""

    encoded_name = quote(character_name, safe="")
    response = client.get(
        f"{API_BASE_URL}/{encoded_name}",
        headers={"accept": "application/json"},
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()

    characters = payload.get("character", {}).get("other_characters", [])
    return [
        Character(
            name=item.get("name", "Unknown"),
            status=item.get("status", "Unknown"),
        )
        for item in characters
    ]


def print_characters(characters: list[Character]) -> None:
    if not characters:
        print("No other characters were returned.")
        return

    for character in characters:
        print(f"- {character.name}: {character.status}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("character", help="character name")
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="request timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--interval",
        type=float,
        help="repeat the query at this interval in seconds",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.interval is not None and args.interval <= 0:
        print("--interval must be greater than zero")
        return 2

    try:
        while True:
            characters = fetch_other_characters(
                args.character,
                timeout=args.timeout,
            )
            print_characters(characters)

            if args.interval is None:
                return 0
            time.sleep(args.interval)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return 1
    except KeyboardInterrupt:
        print("Stopped by user.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
