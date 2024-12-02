class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        left_list = []
        right_list = []

        for line in file_content:
            line_tokens = line.split()

            if len(line_tokens) != 2:
                raise ValueError("Left and Right are not equal in length")

            left_list.append(int(line_tokens[0]))
            right_list.append(int(line_tokens[1]))

        # build a dict of counts
        value_counts: dict[int, int] = {}
        for item in right_list:
            value_count = value_counts.get(item, 0)
            value_count = value_count + 1
            value_counts[item] = value_count

        # calculate the total distance
        total_distance = 0
        for item in left_list:
            value_count = value_counts.get(item, 0)
            distance = item * value_count
            total_distance = total_distance + distance

        return total_distance
