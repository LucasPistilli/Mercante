from fastapi import APIRouter

orders_router = APIRouter(prefix="/orders", tags=["orders"])


@orders_router.get("/pedidos/meus-pedidos/")
async def lista_compras():
    return{"Listagem de pedidos realizada com sucesso!"}

@orders_router.get("/lojas/{loja_id}/pedidos/") 
async def lista_vendas():
    return{"Listagem de vendas da loja realizada com sucesso!"}

@orders_router.get("/pedidos/{pedido_id}/")
async def detalhes_pedido():
    return{"Listagem de detalhes do pedido realizada com sucesso!"}

@orders_router.post("/pedidos/")
async def criar_pedido():
    return{"Pedido cadastrado com sucesso!"}

@orders_router.put("/pedidos/{pedido_id}/status")
async def atualizar_pedido():
    return{"Pedido atualizado comm sucesso"}

