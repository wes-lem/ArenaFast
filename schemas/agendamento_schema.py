from pydantic import BaseModel

class AgendamentoCreate(BaseModel):
    quadra_id: int
    data: str
    hora: str
    nome_responsavel: str

    class Config:
        from_attributes = True