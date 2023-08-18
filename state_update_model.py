from typing import TypedDict


class StatePosition(TypedDict):
    x: int
    y: int


class StateBall(TypedDict):
    pos: StatePosition
    color: str


class Claw(TypedDict):
    pos: StatePosition
    open: bool


class StateModel(TypedDict):
    nofRows: int
    nofCols: int
    balls: list[StateBall]
    claw: Claw

class StateUpdateModel(TypedDict):
    userId: str
    state: StateModel


def getDefaultState() -> StateUpdateModel:
    stateobj: StateUpdateModel = {
        "userId": "glen",
        "state": {"nofRows": 4, "nofCols": 5, "balls": [{"pos": {"x": 3, "y": 4}, "color": "blue"}], "claw": {"pos": {"x": 0, "y": 0}, "open": True}},
    }
    return stateobj
