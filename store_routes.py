from fastapi import APIRouter

store_router = APIRouter(prefix="/store", tags=["store"])

@store_router.post("/lojas/")
async def criar_loja():
    return {"Loja criada com sucesso"}

@store_router.get("/lojas/")
async def listar_lojas():
    return {"Lojas retornadas com sucesso"}

@store_router.get("/lojas/{loja_id}/")
async def informacoes_loja():
    return {"Informações da loja retornadas com sucesso"}

@store_router.put("/lojas/{loja_id}/")
async def atualizar_loja():
    return {"Loja atualizada com sucesso"}