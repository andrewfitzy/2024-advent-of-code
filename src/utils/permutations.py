def get_permutations(input: list[str]) -> list[list[str]]:
    permutations: list[list[str]] = []
    _build_permutations_recursively(input, permutations, 0)
    return permutations


def _build_permutations_recursively(
    input: list[str],
    permutations: list[list[str]],
    index: int,
) -> None:
    if index == len(input) - 1:
        permutations.append(input.copy())

    input_range = range(index, len(input))
    for pointer in input_range:
        _swap(input, index, pointer)
        _build_permutations_recursively(input, permutations, index + 1)
        _swap(input, pointer, index)


def _swap(
    current_value: list[str],
    a: int,
    b: int,
) -> None:
    tmp = current_value[a]
    current_value[a] = current_value[b]
    current_value[b] = tmp
