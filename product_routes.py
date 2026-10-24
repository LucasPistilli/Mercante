from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependes import pegar_sessao
from schemas import ProdutoResponseSchema, ProdutoSchema
from models import Produtos, Loja

product_router = APIRouter(prefix="/product", tags=["product"])

@product_router.post("/lojas/{loja_id}/produtos/", status_code=status.HTTP_201_CREATED)
async def cadastrar_produto(
    loja_id: int,
    produto_schema: ProdutoResponseSchema,
    session: Annotated[Session, Depends(pegar_sessao)]
):
    loja = session.get(Loja, loja_id)
    if not loja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loja não encontrada"
        )

    novo_produto = Produtos(
        loja_id=loja_id,
        nome=produto_schema.nome,
        descricao=produto_schema.descricao,
        quantidade_estoque=produto_schema.quantidade_estoque,
        categoria=produto_schema.categoria,
        valor_unitario=produto_schema.valor_unitario
    )

    session.add(novo_produto)
    session.commit()
    session.refresh(novo_produto) 

    return {
        "mensagem": "Produto cadastrado com sucesso",
        "produto": novo_produto
    }

@product_router.get("/produtos/")
async def listar_produtos(
    loja_id: int,
    session: Annotated[Session, Depends(pegar_sessao)] 
):
    produto = session.query(Produtos).filter(Produtos.loja_id == loja_id).all()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum produto encontrado para esta loja"
        )
    return {
        "Produtos trazidos com sucesso": True,
        "produtos": produto
    }

@product_router.get("/produtos/{produto_id}/")
async def detalhes_produto(
    produto_id: int,
    session: Annotated[Session, Depends(pegar_sessao)]
):
    produto = session.query(Produtos).filter(Produtos.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    return {
        "Detalhes trazidos com sucesso": True,
        "produto": produto
    }

@product_router.put("/produtos/{produto_id}/")
async def atualizar_produto(
    produto_id: int,
    produto_schema: ProdutoSchema,
    session: Annotated[Session, Depends(pegar_sessao)]
):
    produto = session.query(Produtos).filter(Produtos.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    produto.nome = produto_schema.nome
    produto.descricao = produto_schema.descricao
    produto.quantidade_estoque = produto_schema.quantidade_estoque
    produto.categoria = produto_schema.categoria
    produto.valor_unitario = produto_schema.valor_unitario
    
    session.commit()
    session.refresh(produto) 
    
    return {
        "mensagem": "Produto atualizado com sucesso",
        "produto": produto
    }

@product_router.delete("/lojas/{loja_id}/produtos/{produto_id}/")
async def deletar_produto(
    loja_id: int,
    produto_id: int,
    session: Annotated[Session, Depends(pegar_sessao)]
):
    # Verifica se o produto existe e pertence à loja
    produto = session.query(Produtos).filter(
        Produtos.id == produto_id,
        Produtos.loja_id == loja_id
    ).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado ou não pertence à loja"
        )
    session.delete(produto)
    session.commit()
    return {"Produto deletado com sucesso"}







