import asyncio

from ball_control import BallControl, IllegalBallControlStateError

class BallControlSim(BallControl):

    MIN_X = 0
    MIN_Y = 0
    MAX_X = 3
    MAX_Y = 4
    delay_mult = 1.0
    x = 0
    y = 0
    moving_horizontally = False
    moving_vertically = False

    #def __init__(self: BallControl, delay_multiplier: float) ->  None:
    #    self.delay_multiplier = delay_multiplier

    def __set_position(cls, x: int, y: int = 0):
        if (x < cls.MIN_X or y < cls.MIN_Y or x > cls.MAX_X or y > cls.MAX_Y):
            raise Exception("coordinates out of bounds")
        cls.x = x;
        cls.y = y;
        print(f"new position: {cls.x}, {cls.y}")
    
    async def __delay(cls, duration: float):
        await asyncio.sleep(duration * cls.delay_mult)

    async def move_relative(cls, x: int, y: int = 0):
        if (cls.x == x and cls.y == y):
            return
        await cls.__delay(1.0)
        cls.__set_position(cls.x + x, cls.y + y)

    async def move_horizontally(cls, distance: int):
        if (0 == distance):
            return
        if (cls.moving_horizontally):
            raise IllegalBallControlStateError("Already moving horizontally")
        cls.moving_horizontally = True
        try:
            await cls.move_relative(distance)
        finally:
            cls.moving_horizontally = False

    async def move_vertically(cls, distance: int):
        if (0 == distance):
            return
        if (cls.moving_vertically):
            raise IllegalBallControlStateError("Already moving vertically")
        cls.moving_vertically = True
        try:
            await cls.move_relative(0, distance)
        finally:
            cls.moving_vertically = False
            
    def move_horizontally_sync(cls, distance: int):
        asyncio.run(cls.move_horizontally(distance))
    
    def move_vertically_sync(cls, distance: int):
        asyncio.run(cls.move_vertically(distance))

    def move_relative_sync(cls, x: int, y: int = 0):
        asyncio.run(cls.move_relative(x, y))

    def get_position(cls) -> tuple[int, int]:
        return cls.x, cls.y
