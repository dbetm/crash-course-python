from map_reduce import emit_reduce_result, get_reduce_inputs



def reduce(key: str, values: list):
    total = sum(values)

    emit_reduce_result(key, total)


reduce_inputs = get_reduce_inputs()

for key, values in dict(sorted(reduce_inputs.items())).items():
    reduce(key, values)