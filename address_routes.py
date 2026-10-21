from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import requests
from models import db
from models import Enderecos
from database import get_db

address_router = APIRouter(prefix="/enderecos", tags=["Endereços"])

def Buscar_dados_cep(cep : str):
    cep_limpo = cep.replace("-" , "".replace(".", ""))
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
async def adicionar_endereco(entrada: EnderecoEntrada, db: Session = Depends(get_db)):
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
async def listar_enderecos():
    return {"Endereços retornados com sucesso"}

@address_router.delete("/enderecos/{endereco_id}/")
async def remover_endereco():
    return {"Endereço deletado com sucesso"}


