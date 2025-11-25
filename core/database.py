from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings
from models.base import Base
import asyncio
import sys

engine = create_async_engine(settings.DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        asyncio.run(init_db())
