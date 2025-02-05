class Agendamento:
    def __init__(self, id: int, quadra_id: int, data: str, hora: str, nome_responsavel: str):
        self.id = id
        self.quadra_id = quadra_id
        self.data = data
        self.hora = hora
        self.nome_responsavel = nome_responsavel

    def to_dict(self):
        return {
            "id": self.id,
            "quadra_id": self.quadra_id,
            "data": self.data,
            "hora": self.hora,
            "nome_responsavel": self.nome_responsavel
        }