import asyncio
from ball_control import BallControl

async def yoer():
    print("yo")
    await asyncio.sleep(0.14)
    print("yoyyoo")

async def oyer():
    print("oy")
    await asyncio.sleep(1)
    print("oyoyoyoyoy")

def yoer_sync():
    asyncio.run(yoer())

async def main():
    #y = asyncio.create_task(yoer())
    #await oyer()
    #await y
    #yoer_sync()
    await BallControl.move_relative(3)
    await BallControl.move_relative(-1)

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    #yoer_sync()
    elapsed = time.perf_counter() - s
    print(f"\n{__file__} executed in {elapsed:0.2f} seconds.")

