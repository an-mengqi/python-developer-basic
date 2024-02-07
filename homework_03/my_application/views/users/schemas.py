from pydantic import BaseModel
from pydantic import Field
from random import randrange


class PlayerBase(BaseModel):
    playername: str


class PlayerCreate(PlayerBase):
    """
    create player schema
    """


def generate_number():
    return randrange(100)


class PlayerOut(PlayerBase):
    """
        Player Out Schema (API representation)
        """
    id: int = Field(example=123)
    tennis_balls_number: int = Field(default_factory=generate_number)


class Player(PlayerBase):
    id: int
    tennis_balls_number: int = Field(default_factory=generate_number)
