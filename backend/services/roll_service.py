import random

from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models import Game, User


class RollService:
    """Kolmen rullan slotti. Voitto vain 3 samasta. Asetukset DB:stä."""

    def __init__(
        self,
        db: Session,
        *,
        user_name: str = "player1",
        game_name: str = "classic",
    ) -> None:
        self.db = db

        user = db.query(User).filter_by(name=user_name).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User '{user_name}' not found")

        game = db.query(Game).filter_by(name=game_name).first()
        if not game or not game.symbols:
            raise HTTPException(status_code=404, detail=f"Game '{game_name}' not found")

        self.user = user
        self.bet = game.bet
        self._symbols = [s.name for s in game.symbols]
        self._weights = [s.weight for s in game.symbols]
        self._payouts = {s.name: s.payout for s in game.symbols}

    def spin_reel(self) -> str:
        return random.choices(self._symbols, weights=self._weights, k=1)[0]

    def payout_for(self, reels: list[str]) -> float:
        if reels[0] == reels[1] == reels[2]:
            return self._payouts[reels[0]]
        return 0.0

    def roll(self) -> dict:
        if self.user.balance < self.bet:
            raise HTTPException(status_code=400, detail="Insufficient balance")

        reels = [self.spin_reel(), self.spin_reel(), self.spin_reel()]
        payout = self.payout_for(reels)

        self.user.balance = self.user.balance - self.bet + payout
        self.db.commit()
        self.db.refresh(self.user)

        return {
            "user": self.user.name,
            "bet": self.bet,
            "reels": reels,
            "payout": payout,
            "net": payout - self.bet,
            "win": payout > 0,
            "balance": self.user.balance,
        }
