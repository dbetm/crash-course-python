import os
from typing import Dict, List



HOST = os.getenv("HOST")


def get_map_input(filename: str) -> List[str]:
    with open(f"{HOST}/{filename}", "r") as file:
        text = file.readlines()

    return text


def emit_map_result(key: str, value: int):
    with open(f"{HOST}/map_results/{key}.txt", "a") as file:
        file.write(str(value) + "\n")


def get_reduce_inputs() -> Dict[str, List[int]]:
    results_dir = "map_results"
    filenames = os.listdir(results_dir)
    inputs = dict()

    for filename in filenames:
        key = filename.split(".")[0]

        with open(f"{results_dir}/{filename}", "r") as file:
            content = list(map(int, file.readlines()))

            inputs[key] = content

    return inputs


def emit_reduce_result(key: str, value: int):
    if key == "":
        return

    filename = "reduce_results/results.txt"

    with open(filename, "a") as file:
        file.write(f"{key}: {value}\n")