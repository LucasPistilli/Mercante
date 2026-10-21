from sqlalchemy import create_engine, Column , Integer , String , ForeignKey , Boolean , Float ,DateTime, func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from datetime import datetime

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

#Tabela usuarios

class Usuario(Base):
    __tablename__ = "users"

    id = Column ('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
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

class Loja(Base):
    __tablename__ = "Store"

    id = Column ('id', Integer, primary_key=True , autoincrement=True)
    dono_id = Column('dono_id', Integer , ForeignKey(Usuario.id))
    nome_loja = Column('nome_loja', String)
    descricao = Column('descricao', String)
    status_ativa = Column('status_ativa', Boolean , default=True)

    def __init__(self, dono_id , nome_loja , descricao, status_ativa=True):
        self.dono_id = dono_id
        self.nome_loja = nome_loja
        self.descricao = descricao
        self.status_ativa = status_ativa

#Tabela endereços

class Enderecos(Base):
    __tablename__ = "addresses"

    id = Column('id', Integer, primary_key=True , autoincrement=True)
    usuario_id = Column('usuario_id', Integer , ForeignKey(Usuario.id))
    cep = Column('cep', String, nullable=False)
    logradouro = Column('logradouro', String)
    numero = Column('numero', Integer, nullable=False)
    cidade = Column('cidade', String)
    estado = Column('estado', String)

    def __init__(self, usuario_id, cep , logradouro , numero, cidade , estado):
        self.usuario_id = usuario_id
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

#Tabela produtos
class Produtos(Base):
    __tablename__ = "Products"

    id = Column('id', Integer , primary_key=True , autoincrement=True)
    loja_id = Column('loja_id', Integer , ForeignKey(Loja.id))
    nome = Column('nome', String)
    descricao = Column('descricao', String)
    quantidade_estoque = Column('quantidade_estoque' ,Float)
    categoria = Column('categoria', String) 
    
def __init__(self, loja_id , nome , descricao , quantidade_estoque, categoria):
    self.loja_id = loja_id
    self.nome = nome
    self.descricao = descricao
    self.quantidade_estoque = quantidade_estoque
    self.categoria = categoria       


#Tabela Pedidos
class Pedidos(Base):
    __tablename__ = "Orders"

    id = Column('id', Integer, primary_key=True , autoincrement=True)
    usuario_id = Column('usuario_id', Integer , ForeignKey(Usuario.id))
    loja_id = Column('loja_id', Integer , ForeignKey(Loja.id))
    status_pedido = Column('status_pedido', String) #pedentente, pago, enviado, entregue, cancelado
    valor_total = Column('valor_total', Float) #
    frete = Column('Valor_frete', Float) # criar funcao para calcular o valor do frete
    criado_em = Column('criado_em', DateTime, server_default=func.now())

    def __init__(self,usuario_id , loja_id , status_pedido , criado_em):
        self.usuario_id = usuario_id
        self.loja_id = loja_id
        self.criado_em = criado_em
        self.status_pedido = status_pedido #criar funcao para atualizar o status do pedido
        self.valor_total = valor_total #criar funcao para calcular o valor total do pedido

#Tabela itens_pedidos
class Itens_pedidos(Base):
    __tablename__ = "Order_items"

    id = Column ('id', Integer, primary_key=True , autoincrement=True)
    id_pedido = Column ('id_pedido', Integer , ForeignKey(Pedidos.id))
    produto_id = Column ('produto_id', Integer , ForeignKey(Produtos.id))
    quantidade = Column ('quantidade', Integer)
    preco_unitario = Column ('preco_unitario', Float)

    def __init__(self, id_pedido ,produto_id, quantidade , preco_unitario):
        self.id_pedido = id_pedido
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario


#Tabela Avaliações 
class Avaliacoes(Base):
    __tablename__ = "Reviews"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pedido_id = Column('pedido_id', Integer, ForeignKey(Pedidos.id))
    comprador_id = Column('comprador_id', Integer,)
    nota = Column('nota', Integer, nullable=False) # 1 a 5, não pode ter número quebrado, criar a função
    comentario = Column('comentario', String)

def __init__(self, pedido_id , comprador_id, nota , comentario):
    self.pedido_id = pedido_id
    self.comprador_id = comprador_id
    self.nota = nota
    self.comentario = comentario