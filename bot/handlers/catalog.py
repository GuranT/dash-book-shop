from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy import select
from core.database import get_session
from models.base import Product
from bot.keyboards.inline import get_product_kb

router = Router()

@router.message(F.text == "/catalog")
async def catalog(message: Message):
    async with get_session() as s:
        products = (await s.execute(select(Product).where(Product.is_active == True, Product.stock > 0))).scalars().all()
        if not products:
            await message.answer("Товаров пока нет")
            return
        for p in products:
            text = f"<b>{p.title}</b>\nЦена: ${p.price_usd}\nВ наличии: ∞"
            await message.answer(text, reply_markup=get_product_kb(p.id, p.price_usd), parse_mode="HTML")