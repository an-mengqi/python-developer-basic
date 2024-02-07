"""
Create
Read
Update
Delete
"""

from pydantic import BaseModel
from .schemas import Player, PlayerCreate


class Storage(BaseModel):
    players: dict[int, Player] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_player(self, player_in: PlayerCreate) -> Player:
        player = Player(
            id=self.next_id,
            **player_in.model_dump(),)
        self.players[player.id] = player
        return player

    def get_all_players(self) -> list[Player]:
        return list(self.players.values())

    def get_player(self, player_id: int) -> Player | None:
        return self.players.get(player_id)


storage = Storage()
storage.create_player(PlayerCreate(playername="Bob"))
