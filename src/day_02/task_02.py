class Task02:
    RISING: str = "rising"
    FALLING: str = "falling"
    NO_CHANGE: str = "no_change"

    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        safe_report_count = 0
        for report in file_content:
            levels_txt = report.split()

            levels = [int(level) for level in levels_txt]
            safe_report_count = safe_report_count + 1 if cls.is_safe(levels=levels) else safe_report_count

        return safe_report_count

    @classmethod
    def is_safe(cls, levels: list[int]) -> bool:
        # If the report is already ok, return true
        if cls.check_level(levels):
            return True

        # Process a list of processed input
        dampened_levels = cls.apply_problem_dampener(levels)
        for level in dampened_levels:
            # If any pass we have a valid report so return True
            if cls.check_level(level):
                return True

        return False

    @classmethod
    def apply_problem_dampener(cls, levels: list[int]) -> list[list[int]]:
        # build a list of combinations of report
        dampened_levels = []
        i = 0
        while i < len(levels):
            left_part = levels[0:i]
            right_part = levels[i + 1 :]
            dampened_levels.append(left_part + right_part)
            i += 1

        return dampened_levels

    @classmethod
    def check_level(cls, levels: list[int]) -> bool:
        # work out report trajectory
        first = levels[0]
        second = levels[1]
        if first == second:
            return False
        if first > second:
            trajectory = cls.FALLING
        else:
            trajectory = cls.RISING

        # process report
        i = 1
        while i < len(levels):
            previous_number = levels[i - 1]
            current_number = levels[i]
            difference = previous_number - current_number
            if difference == 0:
                return False

            if trajectory == cls.FALLING and (difference < 1 or difference > 3):
                return False

            if trajectory == cls.RISING and (difference < -3 or difference > -1):
                return False
            i += 1

        return True
