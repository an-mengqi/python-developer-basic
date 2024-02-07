from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status
from .crud import storage
from .schemas import PlayerOut, PlayerCreate, Player

router = APIRouter()


@router.get("/", response_model=list[PlayerOut])
def get_all_players():
    return storage.get_all_players()


@router.post("/", response_model=PlayerOut, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerCreate):
    return storage.create_player(player_in=player_in)


@router.get("/{player_id}/",
            response_model=PlayerOut,
            responses={
                status.HTTP_404_NOT_FOUND: {
                    "description": "Player Not Found",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Player #0 Not Found!"}
                        }
                    },
                },
            },
            )
def get_player(player_id: int):
    player: Player | None = storage.get_player(player_id=player_id)
    if player:
        return player
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Player #{player_id} Not Found!"
    )
