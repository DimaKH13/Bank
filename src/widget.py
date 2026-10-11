from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    parts = account_card_info.rsplit(" ", 1)

    if len(parts) < 2:
        return "Некорректный ввод"

    name, number = parts[0], parts[1]

    if len(number) == 16:
        masked = get_mask_card_number(number)
    elif len(number) == 20:
        masked = get_mask_account(number)
    else:
        return "Неверный формат номера"

    return f"{name} {masked}"


def get_date(date_string: str) -> str:
    dt_object = datetime.fromisoformat(date_string)
    return dt_object.strftime("%d.%m.%Y")
