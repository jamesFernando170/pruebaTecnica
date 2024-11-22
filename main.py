from fastapi import FastAPI
from Router.Producto import product
from Router.Category import category

app = FastAPI()

app.include_router(product, prefix="/product")
app.include_router(category, prefix="/product")


