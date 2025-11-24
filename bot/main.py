import asyncio
from aiogram import Bot, Dispatcher
from core.config import settings
from core.database import init_db
from bot.handlers.start import router as start_router
from bot.handlers.catalog import router as catalog_router
from bot.handlers.payment import router as payment_router

async def main():
    await init_db()
    bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router, catalog_router, payment_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())