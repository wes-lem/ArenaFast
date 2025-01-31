import json
from models.agendamento import Agendamento
from datetime import datetime

AGENDAMENTOS_FILE = 'data/agendamentos.json'

def load_agendamentos():
    try:
        with open(AGENDAMENTOS_FILE, 'r') as file:
            data = json.load(file)
            for item in data:
                # Converte as strings ISO 8601 de volta para datetime
                if 'data_hora' in item and isinstance(item['data_hora'], str):
                    item['data_hora'] = datetime.fromisoformat(item['data_hora'])
            return data
    except FileNotFoundError:
        return []

def save_agendamentos(data):
    def custom_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Converte o datetime para string no formato ISO 8601
        raise TypeError(f"Tipo {type(obj)} não é serializável em JSON.")

    with open(AGENDAMENTOS_FILE, 'w') as file:
        json.dump(data, file, indent=4, default=custom_serializer)

def get_all_agendamentos():
    data = load_agendamentos()
    return [Agendamento(**item) for item in data]

def get_agendamento_by_id(agendamento_id: int):
    data = load_agendamentos()
    for item in data:
        if item['id'] == agendamento_id:
            return Agendamento(**item)
    return None  # Retorna None se o agendamento não for encontrado


def create_agendamento(agendamento_data):
    agendamentos = load_agendamentos()
    new_agendamento = Agendamento(**agendamento_data)
    agendamentos.append(new_agendamento.to_dict())
    save_agendamentos(agendamentos)
    return new_agendamento

def add_agendamento(agendamento: dict):
    agendamentos = load_agendamentos()
    agendamento['id'] = len(agendamentos) + 1
    agendamento['data'] = agendamento['data'].isoformat()  # Converte datetime para string ISO 8601
    agendamentos.append(agendamento)
    save_agendamentos(agendamentos)
    return agendamento

def update_agendamento_dao(agendamento_id: int, updated_data: dict):
    agendamentos = load_agendamentos()
    for index, agendamento in enumerate(agendamentos):
        if agendamento['id'] == agendamento_id:
            agendamentos[index].update(updated_data)
            save_agendamentos(agendamentos)
            return agendamentos[index]
    return None

def delete_agendamento(agendamento_id: int):
    agendamentos = load_agendamentos()
    agendamentos = [agendamento for agendamento in agendamentos if agendamento['id'] != agendamento_id]
    save_agendamentos(agendamentos)
    return {"message": "Agendamento deletado com sucesso"}
