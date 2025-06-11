from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declared_attr
from database import Base
from datetime import datetime

class Pessoa(Base):
    __abstract__ = True  # Indica que esta é uma classe base abstrata

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    data_nascimento = Column(DateTime, nullable=True)
    email = Column(String(100), nullable=True)
    telefone = Column(String(11), nullable=True)
    endereco = Column(String(200), nullable=True)
    data_cadastro = Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.nome}>"

class Funcionario(Pessoa):
    cargo = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    data_contratacao = Column(DateTime, nullable=False)
    departamento = Column(String(50), nullable=True)
    ativo = Column(Boolean, default=True)

class Cliente(Pessoa):
    limite_credito = Column(Float, default=0.0)
    pontos_fidelidade = Column(Integer, default=0)
    vip = Column(Boolean, default=False)
    ultima_compra = Column(DateTime, nullable=True) 