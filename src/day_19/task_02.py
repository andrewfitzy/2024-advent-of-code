class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        available_patterns = file_content[0].split(", ")

        designs = file_content[2:]

        possible_designs = 0
        for design in designs:
            possible_designs = possible_designs + cls.get_number_of_possibilities(
                design=design, available_patterns=available_patterns
            )

        return possible_designs

    @classmethod
    def get_number_of_possibilities(cls, design: str, available_patterns: list[str]) -> int:
        tracker: dict[str, int] = {}
        count = cls.find_combos_recursively(design=design, available_patterns=available_patterns, tracker=tracker)
        return count

    @classmethod
    def find_combos_recursively(cls, design: str, available_patterns: list[str], tracker: dict[str, int]) -> int:
        if len(design) == 0:
            return 1
        if design in tracker:
            return tracker[design]
        total = 0
        for available_pattern in available_patterns:
            if design.startswith(available_pattern):
                total += cls.find_combos_recursively(
                    design=design[len(available_pattern) :], available_patterns=available_patterns, tracker=tracker
                )
        tracker[design] = total
        return total
