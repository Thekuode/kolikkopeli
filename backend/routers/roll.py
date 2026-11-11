from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services.roll_service import RollService

router = APIRouter()


@router.get("/roll")
def roll(db: Session = Depends(get_db)):
    return RollService(db).roll()
