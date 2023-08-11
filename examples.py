import asyncio
from ball_control import BallControl
from control_factory import get_control_sim

def single_command(bc: BallControl):
    bc.move_relative_sync(1, 0)

def sequence1(bc: BallControl):
    bc.move_relative_sync(1, 0)
    x, y = bc.get_position()
    print(f"x:{x} y:{y}")
    bc.move_relative_sync(0, 4)
    bc.move_relative_sync(-1, -4)
    x, y = bc.get_position()
    print(f"x:{x} y:{y}")

def sequence2(bc: BallControl):
    bc.move_vertically_sync(2)    
    bc.move_horizontally_sync(3)
    bc.move_vertically_sync(-2)
    bc.move_horizontally_sync(-1)

async def sequence_async(bc: BallControl):
    await bc.move_vertically(2)
    await bc.move_horizontally(3)
    await bc.move_vertically(-2)
    await bc.move_horizontally(-1)

def example_async(bc: BallControl):
    asyncio.run(sequence_async())

async def sequence_concurrent():
    async with get_control_sim() as bc:
       
        t1 = asyncio.create_task(bc.move_vertically(2))
        t2 = asyncio.create_task(bc.move_horizontally(3))
        await t1
        await t2

        t3 = asyncio.create_task(bc.move_vertically(-2))
        t4 = asyncio.create_task(bc.move_horizontally(-1))
        await t3
        await t4

def example_concurrent():
    asyncio.run(sequence_concurrent())
    

def main():
    #single_command()
    #sequence1()
    #sequence2()
    #example_async()
    #bcontrol = get_control_sim()
    example_concurrent()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"\n{__file__} executed in {elapsed:0.2f} seconds.")

