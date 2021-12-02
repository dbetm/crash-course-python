from datetime import datetime

def execution_time(funct):
    # *args -> positional arguments, **kwargs -> no positional arguments
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        funct(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time

        print(f'{time_elapsed.total_seconds()} seconds passed.')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

random_func()
sum(21, 10)
