from fastapi import APIRouter

product_router = APIRouter(prefix="/product", tags=["product"])

@product_router.post("/lojas/{loja_id}/produtos/")
async def cadastrar_produto():
    return {"Produto cadastrado com sucesso"}

@product_router.get("/produtos/")
async def listar_produtos():
    return {"Listagem de produtos realizada com sucesso"}

@product_router.get("/produtos/{produto_id}/")
async def detalhes_produto():
    return {"Detalhes trazidos com sucesso"}

@product_router.put("/produtos/{produto_id}/")
async def atualizar_produto():
    return {"Produto atualizado com sucesso"}

@product_router.delete("/produtos/{produto_id}/")
async def deletar_produto():
    return {"Produto deletado com sucesso"}


