from sqlalchemy import create_engine, Column , Integer , String , ForeignKey , Boolean , Float , Select ,DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

#Tabela usuarios

class Usuario(Base):
    __tablename__ = "users"

    id = Column ('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String),
    email = Column('email', String , nullable=False, unique=True)
    senha = Column('senha', String)
    cpf_cnpj = Column('cpf_cnpj', String, nullable=False, unique=True)
    criado_em = Column('criado_em', DateTime, server_default=func.now())#Esse server_default=func.now fala pro banco que ele irá pegar a data e hora sempre que uma nova linha for inserida


    def __init__(self, nome, email , senha , cpf_cnpj , criado_em):
        self.nome = nome
        self.email = email
        self.senha = senha 
        self.cpf_cnpj = cpf_cnpj
        self.criado_em = criado_em

#Tabela loja

