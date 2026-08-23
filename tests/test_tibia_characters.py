from __future__ import annotations

import unittest

from scripts.tibia_characters import Character, fetch_other_characters


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload
        self.raise_called = False

    def raise_for_status(self) -> None:
        self.raise_called = True

    def json(self) -> dict:
        return self.payload


class FakeClient:
    def __init__(self, payload: dict) -> None:
        self.response = FakeResponse(payload)
        self.request: tuple[str, dict[str, str], float] | None = None

    def get(self, url: str, *, headers: dict[str, str], timeout: float):
        self.request = (url, headers, timeout)
        return self.response


class FetchOtherCharactersTests(unittest.TestCase):
    def test_encodes_name_and_maps_response(self) -> None:
        client = FakeClient(
            {
                "character": {
                    "other_characters": [
                        {"name": "Knight One", "status": "online"},
                        {"name": "Druid Two", "status": "offline"},
                    ]
                }
            }
        )

        result = fetch_other_characters(
            "Main Character",
            timeout=4.0,
            client=client,
        )

        self.assertEqual(
            client.request,
            (
                "https://api.tibiadata.com/v4/character/Main%20Character",
                {"accept": "application/json"},
                4.0,
            ),
        )
        self.assertTrue(client.response.raise_called)
        self.assertEqual(
            result,
            [
                Character(name="Knight One", status="online"),
                Character(name="Druid Two", status="offline"),
            ],
        )

    def test_returns_empty_list_when_field_is_missing(self) -> None:
        client = FakeClient({"character": {}})

        result = fetch_other_characters("Nobody", client=client)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
