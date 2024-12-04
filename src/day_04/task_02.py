class Task02:
    M = "M"
    A = "A"
    S = "S"

    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        puzzle = []
        for line in file_content:
            puzzle.append(list(line))

        answer = 0
        rows = range(len(puzzle))
        cols = range(len(puzzle[0]))

        for row in rows:
            for col in cols:
                if cls.is_xmas_point(puzzle, row, col):
                    answer = answer + 1

        return answer

    @classmethod
    def is_xmas_point(cls, puzzle: list[list[str]], row: int, col: int) -> bool:
        if puzzle[row][col] != cls.A:
            return False

        # build a 3x3 array
        if (
            (row - 1 >= 0 and col - 1 >= 0)
            and (row - 1 >= 0 and col + 1 < len(puzzle[0]))
            and (row + 1 < len(puzzle) and col - 1 >= 0)
            and (row + 1 < len(puzzle) and col + 1 < len(puzzle[0]))
        ):
            square = [
                [puzzle[row - 1][col - 1], puzzle[row - 1][col], puzzle[row - 1][col + 1]],
                [puzzle[row][col - 1], puzzle[row][col], puzzle[row][col + 1]],
                [puzzle[row + 1][col - 1], puzzle[row + 1][col], puzzle[row + 1][col + 1]],
            ]

            return cls.is_x_mas(square)
        return False

    @classmethod
    def is_x_mas(cls, square: list[list[str]]) -> bool:
        if (
            square[0][0] == cls.M
            and square[0][2] == cls.M
            and square[1][1] == cls.A
            and square[2][0] == cls.S
            and square[2][2] == cls.S
        ):
            return True

        if (
            square[0][0] == cls.M
            and square[2][0] == cls.M
            and square[1][1] == cls.A
            and square[0][2] == cls.S
            and square[2][2] == cls.S
        ):
            return True

        if (
            square[2][0] == cls.M
            and square[2][2] == cls.M
            and square[1][1] == cls.A
            and square[0][0] == cls.S
            and square[0][2] == cls.S
        ):
            return True

        if (
            square[0][2] == cls.M
            and square[2][2] == cls.M
            and square[1][1] == cls.A
            and square[0][0] == cls.S
            and square[2][0] == cls.S
        ):
            return True

        return False
