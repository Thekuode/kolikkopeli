import random


class RollService:
    """Kolmen rullan slotti. Voitto vain 3 samasta. RTP ≈ 96 %."""
    # TODO: pitää saada betti DB ja muuttaa sitä. Ja rtp muutos myös DB:ssä.
    # TODO: käyttäjän luonti

    BET = 1

    # Painot yhteensä 100. RTP: 3*(0.28^3)*... + 0.16^3*47 ≈ 0.9608
    SYMBOL_WEIGHTS = {
        "cherry": 39,
        "lemon": 28,
        "bell": 22,
        "diamond": 11,
    }

    PAYOUTS = {
        "cherry": 8.0,
        "lemon": 12.0,
        "bell": 15.0,
        "diamond": 47.0,
    }

    def __init__(self) -> None:
        self._symbols = list(self.SYMBOL_WEIGHTS.keys())
        self._weights = list(self.SYMBOL_WEIGHTS.values())

    def spin_reel(self) -> str:
        return random.choices(self._symbols, weights=self._weights, k=1)[0]

    def payout_for(self, reels: list[str]) -> float:
        if reels[0] == reels[1] == reels[2]:
            return self.PAYOUTS[reels[0]]
        return 0.0

    def roll(self) -> dict:
        reels = [self.spin_reel(), self.spin_reel(), self.spin_reel()]
        payout = self.payout_for(reels)

        return {
            "bet": self.BET,
            "reels": reels,
            "payout": payout,
            "net": payout - self.BET,
            "win": payout > 0,
        }

