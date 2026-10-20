from fastapi import APIRouter

address_router = APIRouter(prefix="/address", tags=["address"])

@address_router.post("/enderecos/")
async def adicionar_endereco():
    return {"Endereço adicionado com sucesso"}

@address_router.get("/enderecos/")
async def listar_enderecos():
    return {"Endereços retornados com sucesso"}

@address_router.delete("/enderecos/{endereco_id}/")
async def remover_endereco():
    return {"Endereço deletado com sucesso"}