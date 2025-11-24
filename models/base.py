from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    price_usd = Column(Float, nullable=False)
    file_url = Column(String(500), nullable=False)
    stock = Column(Integer, default=999)
    is_active = Column(Boolean, default=True)
    sales_count = Column(Integer, default=0)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    dash_address = Column(String(50), unique=True)
    amount_dash = Column(Float)
    amount_usd = Column(Float)
    txid = Column(String(100))
    paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product")