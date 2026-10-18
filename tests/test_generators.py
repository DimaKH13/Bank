import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
        },
    ]


def test_filter_by_currency_usd(sample_transactions: list[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_rub(sample_transactions: list[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_filter_by_currency_empty(sample_transactions: list[dict]) -> None:
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    result = list(transaction_descriptions(sample_transactions))
    assert len(result) == 3
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (
            9999,
            10001,
            ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    assert list(card_number_generator(start, stop)) == expected
