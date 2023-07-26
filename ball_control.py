import asyncio

class IllegalBallControlStateError(Exception):
    "Raised when a control command is issued while a command for movement along the same axis is still being executed"
    pass

class BallControl(object):
    """Interface for controlling a ball manipulator in a grid"""

    async def move_relative(cls, x: int, y: int = 0):
        """Move the manipulator arm"""
        pass

    async def move_horizontally(cls, distance: int):
        """Move the manipulator arm horizontally"""
        pass

    async def move_vertically(cls, distance: int):
        """Move the manipulator arm vertically"""
        pass
            
    def move_horizontally_sync(cls, distance: int):
        """Move the manipulator arm horizontally"""
        pass
    
    def move_vertically_sync(cls, distance: int):
        """Move the manipulator arm vertically"""
        pass

    def move_relative_sync(cls, x: int, y: int = 0):
        """Move the manipulator arm"""
        pass

    def get_position(cls) -> tuple[int, int]:
        pass
