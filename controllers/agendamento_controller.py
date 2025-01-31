from fastapi import APIRouter, HTTPException
from schemas.agendamento_schema import AgendamentoCreate
from services.agendamento_service import fetch_agendamentos, delete_agendamento_service, add_agendamento, update_agendamento_service,fetch_agendamento_by_id
from dao.agendamento_dao import update_agendamento_dao
from datetime import datetime

router = APIRouter()

@router.get('/agendamentos')
def get_agendamentos():
    return fetch_agendamentos()

@router.get('/agendamentos/{agendamento_id}')
def get_agendamento(agendamento_id: int):
    agendamento = fetch_agendamento_by_id(agendamento_id)
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return agendamento

@router.post('/agendamentos')
def create_agendamento(agendamento: AgendamentoCreate):
    try:
        agendamento_data = agendamento.model_dump()
        agendamento_data['data'] = datetime.fromisoformat(agendamento_data['data'])
        return add_agendamento(agendamento_data)
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data inválido. Use ISO 8601.")

@router.delete('/agendamentos/{agendamento_id}')
def delete_agendamento(agendamento_id: int):
    try:
        sucesso = delete_agendamento_service(agendamento_id)
        if sucesso:
            return {"message": "Agendamento deletado com sucesso!"}
        else:
            raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/agendamentos/{agendamento_id}')
def update_agendamento(agendamento_id: int, agendamento: AgendamentoCreate):
    updated_data = agendamento.model_dump()  # Converte o Pydantic para dicionário
    updated_agendamento = update_agendamento_dao(agendamento_id, updated_data)  # Usa a função DAO corretamente
    if not updated_agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return updated_agendamento

