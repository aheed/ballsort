from typing import TypedDict

class StateModel(TypedDict):
    nofRows: int
    nofCols: int
    posX: int
    posY: int
    apa: int

class StateUpdateModel(TypedDict):
    userId: str
    state: StateModel
