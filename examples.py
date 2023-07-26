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
    BallControl.move_horizontally_sync(1)
    BallControl.move_horizontally_sync(1)
    BallControl.move_horizontally_sync(-3)

def main():
    single_command()
    #sequence1()
    sequence2()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"\n{__file__} executed in {elapsed:0.2f} seconds.")

