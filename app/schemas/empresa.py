from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional
from datetime import datetime

class EmpresaBase(BaseModel):
    cnpj: constr(min_length=14, max_length=14) = Field(..., description="CNPJ da empresa (apenas números)")
    razao_social: str = Field(..., max_length=128, description="Razão social da empresa")
    nome_fantasia: Optional[str] = Field(None, max_length=128, description="Nome fantasia da empresa")
    numero_contato: Optional[str] = Field(None, max_length=11, description="Número de telefone de contato")
    email_contato: Optional[EmailStr] = Field(None, max_length=64, description="Email de contato")
    website: Optional[str] = Field(None, max_length=128, description="Website da empresa")

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(BaseModel):
    razao_social: Optional[str] = Field(None, max_length=128)
    nome_fantasia: Optional[str] = Field(None, max_length=128)
    numero_contato: Optional[str] = Field(None, max_length=11)
    email_contato: Optional[EmailStr] = Field(None, max_length=64)
    website: Optional[str] = Field(None, max_length=128)

class EmpresaResponse(EmpresaBase):
    id: int
    data_criacao: datetime = Field(..., description="Data de criação do registro")

    class Config:
        from_attributes = True  # Permite a conversão de objetos SQLAlchemy para Pydantic 