from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload 

from auth_routes import auth_router
from address_routes import address_router
from orders_routes import orders_router
from product_routes import product_router
from store_routes import store_router

app.include_router(auth_router)
app.include_router(address_router)
app.include_router(orders_router)
app.include_router(product_router)
app.include_router(store_router)

