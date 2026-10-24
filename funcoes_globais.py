# funcoes_globais.py
from sqlalchemy.orm import Session
from models import Produtos, Loja

def adicionar_produto_loja(
    session: Session,
    loja_id: int,
    nome: str,
    descricao: str,
    quantidade_estoque: int,
    categoria: str,
    valor_unitario: float
):
    loja = session.query(Loja).filter(Loja.id == loja_id).first()
    if not loja:
        return {"sucesso": False, "mensagem": "Loja não encontrada."}

    novo_produto = Produtos(
        loja_id=loja_id,
        nome=nome,
        descricao=descricao,
        quantidade_estoque=quantidade_estoque,
        categoria=categoria
    )

    session.add(novo_produto)
    session.commit()
    session.refresh(novo_produto)

    return {"sucesso": True, "produto": novo_produto}