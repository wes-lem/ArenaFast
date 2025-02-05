import json
from models.agendamento import Agendamento

AGENDAMENTOS_FILE = "data/agendamentos.json"


def load_agendamentos():
    try:
        with open(AGENDAMENTOS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_agendamentos(data):
    with open(AGENDAMENTOS_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_all_agendamentos():
    data = load_agendamentos()
    return [Agendamento(**item) for item in data]


def get_agendamento_by_id(agendamento_id: int):
    data = load_agendamentos()
    for item in data:
        if item["id"] == agendamento_id:
            return Agendamento(**item)
    return None


def create_agendamento(agendamento_data):
    agendamentos = load_agendamentos()
    new_agendamento = Agendamento(**agendamento_data)
    agendamentos.append(new_agendamento.to_dict())
    save_agendamentos(agendamentos)
    return new_agendamento


def add_agendamento(agendamento: dict):
    agendamentos = load_agendamentos()
    agendamento["id"] = len(agendamentos) + 1
    agendamentos.append(agendamento)  # Mantendo a data como string
    save_agendamentos(agendamentos)
    return agendamento


def update_agendamento_dao(agendamento_id: int, updated_data: dict):
    agendamentos = load_agendamentos()
    for index, agendamento in enumerate(agendamentos):
        if agendamento["id"] == agendamento_id:
            agendamentos[index].update(updated_data)
            save_agendamentos(agendamentos)
            return agendamentos[index]
    return None


def delete_agendamento(agendamento_id: int):
    agendamentos = load_agendamentos()
    agendamentos = [
        agendamento
        for agendamento in agendamentos
        if agendamento["id"] != agendamento_id
    ]
    save_agendamentos(agendamentos)
    return {"message": "Agendamento deletado com sucesso"}