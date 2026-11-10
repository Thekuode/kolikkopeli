from fastapi import APIRouter

from services.roll_service import RollService

router = APIRouter()


@router.get("/roll")
def roll():
    result = RollService().roll()
    return result
