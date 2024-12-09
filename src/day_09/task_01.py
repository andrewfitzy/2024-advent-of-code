class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        # only one line for this puzzle
        tmp_disk_map = list(file_content[0])
        disk_map = [int(bit) for bit in tmp_disk_map]

        exploded_map = cls.explode_map(disk_map)

        defragged_map = cls.defrag_map(exploded_map)

        result = 0
        count = 0
        for item in defragged_map:
            result = (item * count) + result
            count = count + 1

        return result

    @classmethod
    def explode_map(cls, disk_map: list[int]) -> list[int]:
        exploded_map: list[int] = []

        file_id = 0
        position = 1
        free_space = False
        for item_length in disk_map:
            for index in range(item_length):
                if free_space:
                    exploded_map.append(-1)
                else:
                    exploded_map.append(file_id)
            if free_space:
                file_id = file_id + 1
            position = position + 1
            free_space = not free_space
        return exploded_map

    @classmethod
    def defrag_map(cls, exploded_map: list[int]) -> list[int]:
        # Count the number of positive ints in the exploded map
        character_count = 0
        for item in exploded_map:
            if item >= 0:
                character_count = character_count + 1

        front_pointer = 0
        back_pointer = len(exploded_map) - 1
        free_space_count = 0
        defragged_map: list[int] = []
        # While the defrag map has less ints tha the number of ints we need.
        while len(defragged_map) < character_count:
            bit = exploded_map[front_pointer]
            # if int is a -1, move backwards through the list populating the data
            if bit == -1:
                back_bit = exploded_map[back_pointer]
                back_pointer = back_pointer - 1
                while back_bit == -1:
                    back_pointer = back_pointer - 1
                    back_bit = exploded_map[back_pointer]
                    free_space_count = free_space_count + 1
                defragged_map.append(back_bit)
                free_space_count = free_space_count + 1
            else:
                defragged_map.append(bit)

            front_pointer = front_pointer + 1
        return defragged_map
