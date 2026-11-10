from fastapi import APIRouter

router = APIRouter()

@router.get("/roll")
def roll():
    return {"result": "heads"}