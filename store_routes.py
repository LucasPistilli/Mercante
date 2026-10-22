from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependes import pegar_sessao
from models import Usuario,Loja
from schemas import LojaSchema
from typing import Annotated

store_router = APIRouter(prefix="/store", tags=["store"])

@store_router.post("/lojas/")
async def criar_loja(loja_schema:LojaSchema, session: Annotated[Session,Depends(pegar_sessao)]):

    exist_usuario = session.query(Usuario).filter(Usuario.id == loja_schema.dono_id).first()
    print(exist_usuario.cpf_cnpj)

    if len(exist_usuario.cpf_cnpj) != 14:
        return {"Aviso" : "Apenas contas empresariais (CNPJ) podem registrar uma loja"}   
    else:
        if exist_usuario:
            nova_loja = Loja(
                dono_id = loja_schema.dono_id,
                nome_loja= loja_schema.nome_loja,
                descricao = loja_schema.descricao
            )
            session.add(nova_loja)
            session.commit()
            return {"Loja criada com sucesso"}
        else:
            return {"Mensagem" : "Não existe um usuário com este id"}
    

@store_router.get("/lojas/")
async def listar_lojas():
    return {"Lojas retornadas com sucesso"}

@store_router.get("/lojas/{loja_id}/")
async def informacoes_loja():
    return {"Informações da loja retornadas com sucesso"}

@store_router.put("/lojas/{loja_id}/")
async def atualizar_loja():
    return {"Loja atualizada com sucesso"}



# async def criar_conta(nome:str, email:str, senha:str, session = Depends(pegar_sessao)):

#     usuario = session.query(Usuario).filter(Usuario.email == email).first()

#     if usuario:
#         return {"Mensagem" : "Ja existe um usuário com este e-mail"}
#     else:
#         senha_cripto = decrypt_context.hash(senha)
#         novo_usuario = Usuario(nome, email, senha_cripto, usuario)
#         session.add(novo_usuario)
#         session.commit()
#         return {"Mensagem" : "Usuário cadastrado com Sucesso"}