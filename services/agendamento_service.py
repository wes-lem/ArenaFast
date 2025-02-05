from typing import List, Optional
import json

AGENDAMENTOS_FILE = "data/agendamentos.json"

def load_agendamentos():
    try:
        with open(AGENDAMENTOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_agendamentos(agendamentos):
    with open(AGENDAMENTOS_FILE, "w") as f:
        json.dump(agendamentos, f, indent=4)

def fetch_agendamentos() -> List[dict]:
    return load_agendamentos()

def add_agendamento(data: dict) -> dict:
    agendamentos = load_agendamentos()
    new_agendamento = {
        "id": len(agendamentos) + 1,
        "quadra_id": data["quadra_id"],
        "data": data["data"],
        "hora": data["hora"],
        "nome_responsavel": data["nome_responsavel"],
    }
    agendamentos.append(new_agendamento)
    save_agendamentos(agendamentos)
    return new_agendamento

def update_agendamento_service(agendamento_id: int, data: dict) -> Optional[dict]:
    agendamentos = load_agendamentos()
    for agendamento in agendamentos:
        if agendamento["id"] == agendamento_id:
            agendamento.update(data)
            save_agendamentos(agendamentos)
            return agendamento
    return None

def delete_agendamento_service(agendamento_id: int) -> bool:
    agendamentos = load_agendamentos()
    agendamentos_filtrados = [a for a in agendamentos if a["id"] != agendamento_id]

    if len(agendamentos) == len(agendamentos_filtrados):
        return False

    save_agendamentos(agendamentos_filtrados)
    return True

def fetch_agendamento_by_id(agendamento_id: int) -> Optional[dict]:
    agendamentos = load_agendamentos()
    for agendamento in agendamentos:
        if agendamento["id"] == agendamento_id:
            return agendamento
    return None