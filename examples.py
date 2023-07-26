import asyncio
from ball_control import BallControl

def single_command():
    BallControl.move_relative_sync(1, 0)

def sequence1():
    BallControl.move_relative_sync(1, 0)
    x, y = BallControl.get_position()
    print(f"x:{x} y:{y}")
    BallControl.move_relative_sync(0, 4)
    BallControl.move_relative_sync(-1, -4)
    x, y = BallControl.get_position()
    print(f"x:{x} y:{y}")

def sequence2():
    BallControl.move_vertically_sync(2)    
    BallControl.move_horizontally_sync(3)
    BallControl.move_vertically_sync(-2)
    BallControl.move_horizontally_sync(-1)

async def sequence_async():
    await BallControl.move_vertically(2)
    await BallControl.move_horizontally(3)
    await BallControl.move_vertically(-2)
    await BallControl.move_horizontally(-1)

def example_async():
    asyncio.run(sequence_async())

async def sequence_concurrent():
    t1 = asyncio.create_task(BallControl.move_vertically(2))
    t2 = asyncio.create_task(BallControl.move_horizontally(3))
    await t1
    await t2

    t3 = asyncio.create_task(BallControl.move_vertically(-2))
    t4 = asyncio.create_task(BallControl.move_horizontally(-1))
    await t3
    await t4

def example_concurrent():
    asyncio.run(sequence_concurrent())
    

def main():
    #single_command()
    #sequence1()
    #sequence2()
    #example_async()
    example_concurrent()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"\n{__file__} executed in {elapsed:0.2f} seconds.")

