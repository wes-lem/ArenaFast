from pydantic import BaseModel
from datetime import datetime

class AgendamentoCreate(BaseModel):
    quadra_id: int
    data: datetime
    hora: str
    nome_responsavel: str

    class Config:
        from_attributes = True
