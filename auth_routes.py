from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session

from models import Usuario
from dependes import pegar_sessao
from main import bcrypt_context

from schemas import UsuarioSchema
from typing import Annotated

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/usuarios/")
async def cadastro(usuario_schema : UsuarioSchema, session: Annotated[Session,Depends(pegar_sessao)]):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario :
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    else:
        senha_cript = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome , usuario_schema.email, senha_cript) 
        session.add(novo_usuario)   #fazer um verificador se é cpnj ou cpf, para decidir se a pessoa se cadastrou como vendedor ou cliente
        session.commit()
        return{"Mensagem": f"Usuario cadastrado com Sucesso {usuario_schema.email}"}

@auth_router.post("/login/")
async def login(email : str , senha: str, session:Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {}
        
    

@auth_router.get("/usuarios/me/")
async def retorno_dados():
    return {"Mensagem" : "Você acessou a rota de autentificação"}

@auth_router.put("/usuarios/me/")
async def atualizar_dados():
    return {"Dados atualizados"}