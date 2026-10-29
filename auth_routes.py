from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models import Usuario
from dependes import pegar_sessao
from main import bcrypt_context

from schemas import UsuarioSchema
from typing import Annotated

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/usuarios/")
async def cadastro(usuario_schema : UsuarioSchema, session: Annotated[Session,Depends(pegar_sessao)]):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    else:
        usuario_schema.cpf_cnpj = usuario_schema.cpf_cnpj.replace(".","").replace("-","").replace("/","")
        senha_cript = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(nome=usuario_schema.nome , email=usuario_schema.email, senha=senha_cript, cpf_cnpj=usuario_schema.cpf_cnpj) 
        session.add(novo_usuario)   
        session.commit()
        return{"Mensagem": f"Usuario cadastrado com Sucesso {usuario_schema.email}"}

@auth_router.post("/login/")
async def login(email : str , senha: str,session: Annotated[Session, Depends(pegar_sessao)]):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {}
        
@auth_router.get("/usuarios/me/")
async def retorno_dados(usuario_id,session: Annotated[Session, Depends(pegar_sessao)]):
    dados_usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not dados_usuario :
        raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Usuário não encontrado"
                    )
    return dados_usuario
    
@auth_router.put("/usuarios/me/")
async def atualizar_dados(usuario_id : int,usuario_schema : UsuarioSchema, session: Annotated[Session,Depends(pegar_sessao)]):
    atualizar_usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not atualizar_usuario :
            raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuário não encontrado"
                        )
    senha_cript = bcrypt_context.hash(usuario_schema.senha)
    atualizar_usuario.nome = usuario_schema.nome
    atualizar_usuario.email = usuario_schema.email
    atualizar_usuario.senha= senha_cript
    atualizar_usuario.cpf_cnpj = usuario_schema.cpf_cnpj


    session.commit()
    session.refresh(atualizar_usuario)
    return {"Usuário atualizado com sucesso"}
    
