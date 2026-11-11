from sqlalchemy import String, Float, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    balance: Mapped[float] = mapped_column(Float, default=0)
    deposit_count: Mapped[int] = mapped_column(Integer, default=0)


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    bet: Mapped[float] = mapped_column(Float, default=1.0)

    symbols: Mapped[list["Symbol"]] = relationship(back_populates="game")


class Symbol(Base):
    __tablename__ = "symbols"
    __table_args__ = (UniqueConstraint("game_id", "name"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    name: Mapped[str] = mapped_column(String)
    weight: Mapped[int] = mapped_column(Integer)
    payout: Mapped[float] = mapped_column(Float)

    game: Mapped["Game"] = relationship(back_populates="symbols")