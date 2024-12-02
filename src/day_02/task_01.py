class Task01:
    RISING: str = "rising"
    FALLING: str = "falling"

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
