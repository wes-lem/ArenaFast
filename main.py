from fastapi import FastAPI
from controllers.quadra_controller import router as quadra_router
from controllers.agendamento_controller import router as agendamento_router

app = FastAPI()

# Registrando as rotas
app.include_router(quadra_router, tags=['Quadra'])
app.include_router(agendamento_router, tags=['Agendamento'])

@app.get('/')
def read_root():
    return {"message": "Sistema de Agendamento de Quadras"}
