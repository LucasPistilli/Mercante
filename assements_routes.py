from fastapi import APIRouter

assements_router = APIRouter(prefix="/assements", tags=["Assements"])

@assements_router.post("/pedidos/{pedido_id}/avaliacoes/")
async def criar_comentario():
    return {"Comentário criado com sucesso!"}

@assements_router.get("/produtos/{produto_id}/avaliacoes/")
async def listar_comentario():
    return {"Listagem de comentários realizada com sucesso!"}
