import asyncio
from dataclasses import replace

from ball_control import BallControl, IllegalBallControlStateError
from state_update_model import StatePosition, StateUpdateModel, getDefaultState
from update_reporter import UpdateReporter

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
    update_reporter: UpdateReporter

    def __init__(self, update_reporter: UpdateReporter):
        self.update_reporter = update_reporter

    async def __aenter__(self):
        pass
    
    async def __aexit__(self, *_):
        await self.update_reporter.shutdown()

    def __set_position(self, x: int, y: int = 0):
        if (x < self.MIN_X or y < self.MIN_Y or x > self.MAX_X or y > self.MAX_Y):
            raise Exception("coordinates out of bounds")
        self.x = x;
        self.y = y;
        print(f"new position: {self.x}, {self.y}")
    
    async def __delay(self, duration: float):
        await asyncio.sleep(duration * self.delay_mult)

    async def move_relative(self, x: int, y: int = 0):
        
        newX = self.x + x
        newY = self.y + y
        self.__set_position(newX, newY)
        delayTask = asyncio.create_task(self.__delay(1.0))
        
        old_state = getDefaultState() #temp!!!
        # Create a new instance with the Claw's "open" attribute set to False
        #new_state = replace(old_state, claw=replace(old_state.claw, open=False))
        new_state = replace(old_state, claw=replace(old_state.claw, pos=StatePosition(x = newX, y = newY)))

        state_update: StateUpdateModel = StateUpdateModel(
            userId="glen",
            state=new_state
        )

        await self.update_reporter.send_update(state_update)
        await delayTask

    async def move_horizontally(self, distance: int):
        if (0 == distance):
            return
        if (self.moving_horizontally):
            raise IllegalBallControlStateError("Already moving horizontally")
        self.moving_horizontally = True
        try:
            await self.move_relative(distance)
        finally:
            self.moving_horizontally = False

    async def move_vertically(self, distance: int) -> None:
        if (0 == distance):
            return
        if (self.moving_vertically):
            raise IllegalBallControlStateError("Already moving vertically")
        self.moving_vertically = True
        try:
            await self.move_relative(0, distance)
        finally:
            self.moving_vertically = False
            
    def move_horizontally_sync(self, distance: int):
        asyncio.run(self.move_horizontally(distance))
    
    def move_vertically_sync(self, distance: int):
        asyncio.run(self.move_vertically(distance))

    def move_relative_sync(self, x: int, y: int = 0):
        asyncio.run(self.move_relative(x, y))

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y
