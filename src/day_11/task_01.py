# Standard Library
import math


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        # input is a single line
        start_runes_str = file_content[0]

        runes_list = [int(number) for number in start_runes_str.split(" ")]
        runes: dict[int, int] = {}
        for rune in runes_list:
            rune_count = runes.get(rune, 0)
            rune_count = rune_count + 1
            runes[rune] = rune_count

        count = 0
        while count < 25:
            runes = cls.blink(runes)
            count = count + 1

        rune_count = 0
        for key, value in runes.items():
            rune_count = rune_count + value

        return rune_count

    @classmethod
    def blink(cls, runes: dict[int, int]) -> dict[int, int]:
        new_configuration: dict[int, int] = {}
        for key, value in runes.items():
            if key == 0:
                # move the runes in 0 to 1
                rune_count = new_configuration.get(1, 0)
                rune_count = rune_count + value
                new_configuration[1] = rune_count
                continue

            number_of_digits = cls.count_digits(key)
            if number_of_digits % 2 == 0:
                key_str = str(key)
                mid = math.floor(number_of_digits / 2)
                length = len(key_str)
                left = int(key_str[0:mid])
                right = int(key_str[mid:length])

                rune_count = new_configuration.get(left, 0)
                rune_count = rune_count + value
                new_configuration[left] = rune_count

                rune_count = new_configuration.get(right, 0)
                rune_count = rune_count + value
                new_configuration[right] = rune_count

                continue

            rune_product = key * 2024

            rune_count = new_configuration.get(rune_product, 0)
            rune_count = rune_count + value
            new_configuration[rune_product] = rune_count

        return new_configuration

    @classmethod
    def count_digits(cls, rune: int) -> int:
        # avoid 0 / 10
        if rune == 0:
            return 1

        number_of_digits = 0
        while rune != 0:
            rune = rune // 10
            number_of_digits += 1
        return number_of_digits
