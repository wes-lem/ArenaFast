class Quadra:
    def __init__(self, id: int, tipo: str, capacidade: int):
        self.id = id
        self.tipo = tipo  # Pode ser 'beach-tenis', 'volei' ou 'futsal'
        self.capacidade = capacidade

    def to_dict(self):
        return {"id": self.id, "tipo": self.tipo, "capacidade": self.capacidade}
