from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependes import pegar_sessao
from funcoes_globais import adicionar_produto_loja
from schemas import ProdutoSchema

product_router = APIRouter(prefix="/product", tags=["product"])

@product_router.post("/lojas/{loja_id}/produtos/", status_code=status.HTTP_201_CREATED)
async def cadastrar_produto(
    loja_id: int,
    produto_schema: ProdutoSchema,
    session: Annotated[Session, Depends(pegar_sessao)]
):
    # Chama a função global que salva no models.py
    resultado = adicionar_produto_loja (
        session=session,
        loja_id=loja_id,
        nome=produto_schema.nome,
        descricao=produto_schema.descricao,
        quantidade_estoque=produto_schema.quantidade_estoque,
        categoria=produto_schema.categoria,
        valor_unitario=produto_schema.valor_unitario
    )

    if not resultado["sucesso"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=resultado["mensagem"]
        )

    return {
        "mensagem": "Produto cadastrado com sucesso",
        "produto": resultado["produto"]
    }

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







