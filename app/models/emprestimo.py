from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class StatusEmprestimo(enum.Enum):
    PENDENTE = "pendente"
    EM_ANDAMENTO = "em_andamento"
    DEVOLVIDO = "devolvido"
    ATRASADO = "atrasado"
    CANCELADO = "cancelado"

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    livro_id = Column(Integer, ForeignKey('livro.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), nullable=False)
    
    data_emprestimo = Column(DateTime, default=datetime.utcnow, nullable=False)
    data_prevista_devolucao = Column(DateTime, nullable=False)
    data_devolucao = Column(DateTime, nullable=True)
    
    status = Column(Enum(StatusEmprestimo), default=StatusEmprestimo.PENDENTE)
    valor_multa = Column(Float, default=0.0)
    observacoes = Column(String(500), nullable=True)
    
    # Relacionamentos
    livro = relationship("Livro", backref="emprestimos")
    cliente = relationship("Cliente", backref="emprestimos")
    funcionario = relationship("Funcionario", backref="emprestimos_realizados")

    def __repr__(self):
        return f"<Emprestimo {self.id} - Livro: {self.livro.titulo if self.livro else 'N/A'}>"

    def calcular_multa(self):
        if self.status == StatusEmprestimo.ATRASADO and self.data_devolucao:
            dias_atraso = (self.data_devolucao - self.data_prevista_devolucao).days
            if dias_atraso > 0:
                # Exemplo: R$ 2,00 por dia de atraso
                self.valor_multa = dias_atraso * 2.0
            return self.valor_multa
        return 0.0 