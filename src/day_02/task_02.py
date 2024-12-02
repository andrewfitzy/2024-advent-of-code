class Task02:
    RISING: str = "rising"
    FALLING: str = "falling"
    NO_CHANGE: str = "no_change"

    def solve(self, file_content):
        safe_report_count = 0
        for report in file_content:
            levels_txt = report.split()

            levels = [int(level) for level in levels_txt]
            safe_report_count = safe_report_count + 1 if self.is_safe(levels=levels) else safe_report_count

        return safe_report_count

    def is_safe(self, levels) -> bool:
        # If the report is already ok, return true
        if self.check_level(levels):
            return True

        # Process a list of processed input
        dampened_levels = self.apply_problem_dampener(levels)
        for level in dampened_levels:
            # If any pass we have a valid report so return True
            if self.check_level(level):
                return True

        return False

    def apply_problem_dampener(self, levels):
        # build a list of combinations of report
        dampened_levels = []
        i = 0
        while i < len(levels):
            left_part = levels[0:i]
            right_part = levels[i + 1 :]
            dampened_levels.append(left_part + right_part)
            i += 1

        return dampened_levels

    def check_level(self, levels) -> bool:
        # work out report trajectory
        first = levels[0]
        second = levels[1]
        if first == second:
            return False
        if first > second:
            trajectory = self.FALLING
        else:
            trajectory = self.RISING

        # process report
        i = 1
        while i < len(levels):
            previous_number = levels[i - 1]
            current_number = levels[i]
            difference = previous_number - current_number
            if difference == 0:
                return False

            if trajectory == self.FALLING and (difference < 1 or difference > 3):
                return False

            if trajectory == self.RISING and (difference < -3 or difference > -1):
                return False
            i += 1

        return True
