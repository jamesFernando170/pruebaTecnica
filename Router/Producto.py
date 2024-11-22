from http.client import HTTPException

from fastapi import APIRouter

from Modelos.models import productsModel
from Schema.Product import productSchema
from util.dbAlchemy import session

product = APIRouter()


@product.get("/all")
async def get_productos():
    products = session.query(productsModel).all()
    return products


@product.post("/")
async def get_productos(product: productSchema):
    product_create = productsModel(**product.model_dump())
    product_query = session.query(product_create).filter_by(id=product_create.id)

    if product_query:
        raise HTTPException("Usuario ya existe")
    else:
        session.add(product_create)
        session.commit()
        session.refresh(product_create)
        return product_create
