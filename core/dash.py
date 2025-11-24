import aiohttp
from core.config import settings
from models.base import Order, Product
from core.database import get_session
from aiogram import Bot

bot = Bot(token=settings.BOT_TOKEN)

async def get_dash_price():
    async with aiohttp.ClientSession() as s:
        async with s.get("https://api.blockcypher.com/v1/dash/main") as r:
            data = await r.json()
            return float(data["last"])

async def create_dash_payment(user_id: int, product_id: int, price_usd: float):
    dash_price = await get_dash_price()
    amount_dash = round(price_usd / dash_price, 6)
    async with aiohttp.ClientSession() as s:
        async with s.post(f"https://api.blockcypher.com/v1/dash/main/addrs?token={settings.BLOCKCYPHER_TOKEN}") as r:
            data = await r.json()
            address = data["address"]
    async with get_session() as s:
        order = Order(user_id=user_id, product_id=product_id, dash_address=address,
                      amount_dash=amount_dash, amount_usd=price_usd)
        s.add(order)
        await s.commit()
        await s.refresh(order)
    return address, amount_dash, order.id

async def process_dash_webhook(payload: dict):
    if payload.get("confirmations", 0) < 1:
        return
    address = payload["outputs"][0]["addresses"][0]
    value_dash = sum(o["value"] for o in payload["outputs"] if address in o.get("addresses", [])) / 1e8
    async with get_session() as s:
        order = (await s.execute(
            Order.__table__.select().where(Order.dash_address == address, Order.paid == False)
        )).scalar_one_or_none()
        if not order or value_dash < order.amount_dash * 0.98:
            return
        order.paid = True
        order.txid = payload["hash"]
        product = await s.get(Product, order.product_id)
        product.sales_count += 1
        if product.stock != 999:
            product.stock -= 1
        s.add(order)
        s.add(product)
        await s.commit()
        await bot.send_message(order.user_id,
            f"Оплачено!\n<b>{product.title}</b>\n{product.file_url}",
            parse_mode="HTML")