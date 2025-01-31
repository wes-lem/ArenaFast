from fastapi import APIRouter
from services.quadra_service import fetch_quadras

router = APIRouter()

@router.get('/quadras')
def get_quadras():
    return fetch_quadras()