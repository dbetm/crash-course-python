from typing import List
from map_reduce import get_map_input, emit_map_result


def process_line(text: str) -> dict:
    coincidences = dict()

    for char in text:
        char_lowered = char.lower()

        if char_lowered >= "a" and char_lowered <= "z":
            if char_lowered in coincidences:
                coincidences[char_lowered] += 1
            else:
                coincidences[char_lowered] = 1

    return coincidences


def map_(content: List[str]) -> None:
    for line in content:
        coincidences = process_line(line)

        for key, value in coincidences.items():
            emit_map_result(key, value)


map_input = get_map_input("dataset.txt")
map_(map_input)