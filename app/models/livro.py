from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Livro(Base):
    __tablename__ = "livro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(100), nullable=False)
    isbn = Column(String(13), nullable=False, unique=True)
    editora = Column(String(100), nullable=True)
    ano_publicacao = Column(Integer, nullable=True)
    numero_paginas = Column(Integer, nullable=True)
    preco = Column(Float, nullable=True)
    quantidade_estoque = Column(Integer, default=0)
    data_cadastro = Column(DateTime, default=datetime.utcnow)
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=True)
    
    # Relacionamento com a tabela de categoria
    categoria = relationship("Livro.Categoria", back_populates="livros")

    def __repr__(self):
        return f"<Livro {self.titulo}>"

    class Categoria(Base):
        __tablename__ = "categoria"

        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(50), nullable=False, unique=True)
        descricao = Column(Text, nullable=True)
        
        # Relacionamento com a tabela de livros
        livros = relationship("Livro", back_populates="categoria")

        def __repr__(self):
            return f"<Categoria {self.nome}>" 