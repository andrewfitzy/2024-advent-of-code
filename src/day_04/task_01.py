class Task01:
    XMAS = ["X", "M", "A", "S"]

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
                answer = answer + cls.count_xmas_round_point(puzzle, row, col)

        return answer

    @classmethod
    def count_xmas_round_point(cls, puzzle: list[list[str]], row: int, col: int) -> int:
        count = 0
        if puzzle[row][col] != cls.XMAS[0]:
            return count

        # check from here up-left
        if (row + 1) - len(cls.XMAS) >= 0 and (col + 1) - len(cls.XMAS) >= 0:
            has_xmas_up_left = True
            for i in range(len(cls.XMAS)):
                if puzzle[row - i][col - i] != cls.XMAS[i]:
                    has_xmas_up_left = False
                    break
            if has_xmas_up_left:
                count = count + 1
        # check from here up
        if (row + 1) - len(cls.XMAS) >= 0:
            has_xmas_up = True
            for i in range(len(cls.XMAS)):
                if puzzle[row - i][col] != cls.XMAS[i]:
                    has_xmas_up = False
                    break
            if has_xmas_up:
                count = count + 1
        # check from here up-right
        if (row + 1) - len(cls.XMAS) >= 0 and (col) + len(cls.XMAS) <= len(puzzle[0]):
            has_xmas_up_right = True
            for i in range(len(cls.XMAS)):
                if puzzle[row - i][col + i] != cls.XMAS[i]:
                    has_xmas_up_right = False
                    break
            if has_xmas_up_right:
                count = count + 1
        # check from here left
        if (col + 1) - len(cls.XMAS) >= 0:
            has_xmas_left = True
            for i in range(len(cls.XMAS)):
                if puzzle[row][col - i] != cls.XMAS[i]:
                    has_xmas_left = False
                    break
            if has_xmas_left:
                count = count + 1
        # check from here right
        if (col) + len(cls.XMAS) <= len(puzzle[0]):
            has_xmas_right = True
            for i in range(len(cls.XMAS)):
                if puzzle[row][col + i] != cls.XMAS[i]:
                    has_xmas_right = False
                    break
            if has_xmas_right:
                count = count + 1
        # check from here bottom-left
        if (row) + len(cls.XMAS) <= len(puzzle) and (col + 1) - len(cls.XMAS) >= 0:
            has_xmas_down_left = True
            for i in range(len(cls.XMAS)):
                if puzzle[row + i][col - i] != cls.XMAS[i]:
                    has_xmas_down_left = False
                    break
            if has_xmas_down_left:
                count = count + 1
        # check from here bottom
        if (row) + len(cls.XMAS) <= len(puzzle):
            has_xmas_down = True
            for i in range(len(cls.XMAS)):
                if puzzle[row + i][col] != cls.XMAS[i]:
                    has_xmas_down = False
                    break
            if has_xmas_down:
                count = count + 1
        # check from here bottom-right
        if (row) + len(cls.XMAS) <= len(puzzle) and (col) + len(cls.XMAS) <= len(puzzle[0]):
            has_xmas_down_right = True
            for i in range(len(cls.XMAS)):
                if puzzle[row + i][col + i] != cls.XMAS[i]:
                    has_xmas_down_right = False
                    break
            if has_xmas_down_right:
                count = count + 1

        return count
