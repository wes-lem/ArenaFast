from typing import List, Optional
from datetime import datetime
import json

AGENDAMENTOS_FILE = 'data/agendamentos.json'

def load_agendamentos():
    try:
        with open(AGENDAMENTOS_FILE, 'r') as file:
            data = json.load(file)
            for agendamento in data:
                # Converte a string ISO 8601 para datetime
                if 'data' in agendamento and isinstance(agendamento['data'], str):
                    agendamento['data'] = datetime.fromisoformat(agendamento['data'])
            return data
    except FileNotFoundError:
        return []

# Salvar os agendamentos no arquivo JSON
def save_agendamentos(agendamentos):
    # Converte a data de datetime para string antes de salvar
    for agendamento in agendamentos:
        agendamento['data'] = agendamento['data'].strftime('%Y-%m-%d')
    
    with open(AGENDAMENTOS_FILE, 'w') as f:
        json.dump(agendamentos, f, indent=4)

def fetch_agendamentos() -> List[dict]:
    agendamentos = load_agendamentos()
    return agendamentos

def add_agendamento(data: dict) -> dict:
    agendamentos = load_agendamentos()
    new_agendamento = {
        "id": len(agendamentos) + 1,
        "quadra_id": data['quadra_id'],
        "data": data['data'],
        "hora": data['hora'],
        "nome_responsavel": data['nome_responsavel']
    }
    agendamentos.append(new_agendamento)
    save_agendamentos(agendamentos)
    return new_agendamento

def update_agendamento_service(agendamento_id: int, data: dict) -> Optional[dict]:
    agendamentos = load_agendamentos()
    for agendamento in agendamentos:
        if agendamento['id'] == agendamento_id:
            agendamento.update(data)
            save_agendamentos(agendamentos)
            return agendamento
    return None

def delete_agendamento_service(agendamento_id: int) -> bool:
    agendamentos = load_agendamentos()
    agendamentos_filtrados = [a for a in agendamentos if a["id"] != agendamento_id]

    if len(agendamentos) == len(agendamentos_filtrados):
        return False  # Não encontrou o agendamento

    save_agendamentos(agendamentos_filtrados)
    return True  # Sucesso ao deletar

def fetch_agendamento_by_id(agendamento_id: int) -> Optional[dict]:
    agendamentos = load_agendamentos()
    for agendamento in agendamentos:
        if agendamento['id'] == agendamento_id:
            return agendamento
    return None

def create_agendamento(agendamento_data):
    agendamentos = load_agendamentos()
    new_agendamento = {
        "id": len(agendamentos) + 1,
        "quadra_id": agendamento_data['quadra_id'],
        "data": agendamento_data['data'].strftime('%Y-%m-%d'),  # Converte a data para string
        "hora": agendamento_data['hora'],
        "nome_responsavel": agendamento_data['nome_responsavel']
    }
    agendamentos.append(new_agendamento)
    save_agendamentos(agendamentos)
    return new_agendamento