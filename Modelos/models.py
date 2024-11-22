from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base


class productsModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")


class categoryModel(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    nameCategory = Column(String)
