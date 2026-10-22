from pydantic import BaseModel , EmailStr

class UsuarioSchema(BaseModel):

    nome: str
    email : EmailStr
    senha: str
    cpf_cnpj : str

class Config:
    from_attributes = True


class LojaSchema(BaseModel):
    dono_id: int
    nome_loja: str
    descricao: str
