class Task01:
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

        # sort both arrays
        left_list.sort()
        right_list.sort()

        total_distance = 0
        # iterate through array, compare each and calculate the distace
        for index in range(len(left_list)):
            distance = abs(left_list[index] - right_list[index])
            total_distance = total_distance + distance

        # sum the difference
        return total_distance
