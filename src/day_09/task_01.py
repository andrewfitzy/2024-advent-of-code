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
            result = (int(item) * count) + result
            count = count + 1

        return result

    @classmethod
    def explode_map(cls, disk_map: list[int]) -> list[str]:
        exploded_map: list[str] = []

        file_id = 0
        position = 1
        free_space = False
        for item_length in disk_map:
            for index in range(item_length):
                if free_space:
                    exploded_map.append(".")
                else:
                    exploded_map.append(str(file_id))
            if free_space:
                file_id = file_id + 1
            position = position + 1
            free_space = not free_space
        return exploded_map

    @classmethod
    def defrag_map(cls, exploded_map: list[str]) -> list[str]:
        defragged_map = []
        blanks = []
        for index, bit in enumerate(exploded_map):
            if bit == ".":
                blanks.append(index)
            defragged_map.append(bit)

        for index in blanks:
            while defragged_map[-1] == ".":
                defragged_map.pop(-1)
            if len(defragged_map) <= index:
                break
            defragged_map[index] = defragged_map.pop()

        return defragged_map
