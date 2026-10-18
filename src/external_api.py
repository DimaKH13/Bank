import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли."""
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount", "0")
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")
    amount = float(amount_str)

    if currency_code == "RUB":
        return amount

    url = (
        "https://api.apilayer.com/exchangerates_data/"
        f"latest?symbols=RUB&base={currency_code}"
    )
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    rate = data.get("rates", {}).get("RUB", 1.0)
    return amount * float(rate)
