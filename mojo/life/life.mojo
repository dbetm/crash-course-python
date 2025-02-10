from time import sleep
from gridv1 import Grid


def run_display(owned grid: Grid) -> None:
    while True:
        print(String(grid))
        print()
        sleep(Float64(0.5))
        # if input("Enter 'q' to quit or press <Enter> to continue: ") == "q":
        #     break
        grid = grid.evolve()


def main():
    num_rows = 16
    num_cols = 16
    start = Grid.random(num_rows, num_cols)
    run_display(start)