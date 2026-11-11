from db.database import SessionLocal, init_db
from db.models import User, Game, Symbol


def seed() -> None:
    init_db()
    db = SessionLocal()
    try:
        if not db.query(User).filter_by(name="player1").first():
            db.add(User(name="player1", balance=100.0, deposit_count=1))

        game = db.query(Game).filter_by(name="classic").first()
        if not game:
            game = Game(name="classic", bet=1.0)
            db.add(game)
            db.flush()

            db.add_all([
                Symbol(game_id=game.id, name="cherry", weight=39, payout=8.0),
                Symbol(game_id=game.id, name="lemon", weight=28, payout=12.0),
                Symbol(game_id=game.id, name="bell", weight=22, payout=15.0),
                Symbol(game_id=game.id, name="diamond", weight=11, payout=47.0),
            ])

        db.commit()
        print("Seed OK")
    finally:
        db.close()


if __name__ == "__main__":
    seed()