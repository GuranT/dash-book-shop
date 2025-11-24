from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_product_kb(product_id: int, price: float):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=f"Купить за ${price}", callback_data=f"buy_{product_id}")
    ]])