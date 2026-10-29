from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import requests
from starlette import status
from models import Enderecos , Usuario
from dependes import pegar_sessao
from schemas import UsuarioSchema

address_router = APIRouter(prefix="/enderecos", tags=["Endereços"])

def Buscar_dados_cep(cep : str):
    cep_limpo = cep.replace("-" , "").replace(".", "")
    resposta = requests.get(f"https://viacep.com.br/ws/{cep_limpo}/json/")

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            return dados
        return None

class EnderecoEntrada(BaseModel):
    usuario_id: int
    cep: str
    numero : int

@address_router.post("/")
async def adicionar_endereco(entrada: EnderecoEntrada, db: Session = Depends(pegar_sessao)):
    
    dados_viacep = Buscar_dados_cep(entrada.cep)

    if not dados_viacep:
        raise HTTPException(status_code=400, detail="CEP inválido ou não encontrado.")

    novo_endereco = Enderecos(
        usuario_id = entrada.usuario_id,
        cep = entrada.cep,
        numero = entrada.numero,
        logradouro = dados_viacep["logradouro"],
        cidade = dados_viacep["localidade"],
        estado = dados_viacep["uf"]    )

    db.add(novo_endereco)
    db.commit()
    db.refresh(novo_endereco)

    return {"mensagem": "Endereço adicionado com sucesso", "endereco": novo_endereco}




@address_router.get("/enderecos/")
async def listar_enderecos(session: Annotated[Session,Depends(pegar_sessao)]):
    listar = session.query(Enderecos).filter(Usuario.id == Enderecos.usuario_id).all()
    return listar

@address_router.delete("/enderecos/{endereco_id}/")
async def remover_endereco(endereco_id: int , usuario_id : int,  session: Annotated[Session, Depends(pegar_sessao)]):
    deletar = session.query(Enderecos).filter(Enderecos.usuario_id == usuario_id, Enderecos.id == endereco_id).first()
    if not deletar:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Endereço não encontrado ou não pertence ao Usuario"
            )
    session.delete(deletar)
    session.commit()
    return {"Endereço deletado com sucesso"}
    

    


