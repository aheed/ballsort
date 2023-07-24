import asyncio

class BallControl(object):

    MIN_X = 0
    MIN_Y = 0
    MAX_X = 3
    MAX_Y = 4
    delay_mult = 0.8
    x = 0
    y = 0

    #def __init__(self: BallControl, delay_multiplier: float) ->  None:
    #    self.delay_multiplier = delay_multiplier

    @classmethod
    def __set_position(cls, x: int, y: int = 0):
        if (x < cls.MIN_X or y < cls.MIN_Y or x > cls.MAX_X or y > cls.MAX_Y):
            raise Exception("coordinates out of bounds")
        cls.x = x;
        cls.y = y;
        print(f"new position: {cls.x}, {cls.y}")
    
    @classmethod
    async def __delay(cls, duration: float):
        await asyncio.sleep(duration * cls.delay_mult)

    @classmethod
    async def move_relative(cls, x: int, y: int = 0):
        await cls.__delay(1.0)
        cls.__set_position(cls.x + x, cls.y + y)    
