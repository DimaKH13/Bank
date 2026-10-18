import logging
import os

os.makedirs("logs", exist_ok=True)

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

if not masks_logger.handlers:
    masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    if len(card_number) < 16:
        masks_logger.error(f"Некорректная длина номера карты: {len(card_number)}")
    else:
        masks_logger.info(f"Успешно замаскирован номер карты: {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    if len(account_number) < 4:
        masks_logger.error(f"Некорректная длина номера счета: {len(account_number)}")
    else:
        masks_logger.info(f"Успешно замаскирован номер счета: {account_number[-4:]}")
    return f"**{account_number[-4:]}"
