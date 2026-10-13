import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_valid(input_string: str, expected: str) -> None:
    assert mask_account_card(input_string) == expected


def test_mask_account_card_no_space() -> None:
    assert mask_account_card("НекорректнаяСтрока") == "Некорректный ввод"


def test_mask_account_card_wrong_length() -> None:
    assert mask_account_card("Visa 12345") == "Неверный формат номера"


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected