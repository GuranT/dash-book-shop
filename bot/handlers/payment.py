from aiogram import Router, F
from aiogram.types import CallbackQuery
from core.dash import create_dash_payment
from core.database import get_session
from models.base import Product

router = Router()

@router.callback_query(F.data.startswith("buy_"))
async def buy(call: CallbackQuery):
    product_id = int(call.data.split("_")[1])
    async with get_session() as s:
        product = await s.get(Product, product_id)
        if not product or (product.stock != 999 and product.stock <= 0):
            await call.answer("Нет в наличии", show_alert=True)
            return
        address, amount_dash, _ = await create_dash_payment(
            call.from_user.id, product_id, product.price_usd
        )
        text = f"<b>{product.title}</b>\nЦена: ${product.price_usd}\n\nОтправьте ровно:\n<code>{amount_dash:.6f} DASH</code>\n\nАдрес:\n<code>{address}</code>\n\nПосле 1 подтверждения — ссылка придёт автоматически"
        await call.message.edit_text(text, parse_mode="HTML")
        await call.answer()