# Standard Library
from collections import deque


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        available_patterns = file_content[0].split(", ")

        designs = file_content[2:]

        possible_designs = 0
        for design in designs:
            if cls.is_design_possible(design, available_patterns):
                possible_designs = possible_designs + 1

        return possible_designs

    @classmethod
    def is_design_possible(cls, design: str, available_patterns: list[str]) -> bool:
        # use bfs type processing here to whittle down the designs
        design_queue: deque[str] = deque()
        design_queue.append(design)

        seen = set()
        seen.add(design)
        count = 0
        while len(design_queue) > 0:
            tmp_design = design_queue.popleft()
            for pattern in available_patterns:
                if tmp_design.startswith(pattern):
                    new_design = tmp_design[len(pattern) :]
                    if new_design in seen:
                        continue

                    if len(new_design) == 0:
                        return True
                    design_queue.append(new_design)
                    seen.add(new_design)
            count = count + 1
        return False
