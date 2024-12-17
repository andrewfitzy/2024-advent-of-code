class FileEntry:
    content: str
    length: int

    def __init__(self, content: str, length: int):
        self.content = content
        self.length = length

    def __str__(self):
        return "({content}, {length})".format(content=self.content, length=self.length)


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        # only one line for this puzzle
        tmp_disk_map = list(file_content[0])
        disk_map = [int(bit) for bit in tmp_disk_map]

        map_analysis: dict[int, list[FileEntry]] = cls.analyse_map(disk_map)

        defragged_map = cls.defrag_map(map_analysis)

        decoded_map = cls.decode_analysis(defragged_map)

        result = 0
        count = 0
        for item in decoded_map:
            if len(item) > 0 and item.find(".") == -1:
                chk_part = int(item) * count

                result = chk_part + result
            count = count + 1

        return result

    @classmethod
    def analyse_map(cls, disk_map: list[int]) -> dict[int, list[FileEntry]]:
        map_pointers: dict[int, list[FileEntry]] = {}
        file_id = 0
        block_count = 0
        free_space = False
        for item_length in disk_map:
            if free_space:
                file_id = file_id + 1

            map_pointers[block_count] = [
                FileEntry(
                    content="." if free_space else str(file_id),
                    length=item_length,
                )
            ]
            block_count = block_count + 1
            free_space = not free_space

        return map_pointers

    @classmethod
    def defrag_map(cls, map_analysis: dict[int, list[FileEntry]]) -> dict[int, list[FileEntry]]:
        back_pointer = 0
        blanks = []
        files = []
        for key, values in map_analysis.items():
            if values[0].content == ".":
                blanks.append(key)
            else:
                files.append(key)

            if key > back_pointer:
                back_pointer = key

        blanks.sort()
        files.sort()
        files.reverse()

        file_pointer = 0
        while file_pointer < len(files):
            file_position = files[file_pointer]
            # can't move a file to a file block so file blocks always start with 1 item
            file_block = map_analysis[file_position][0]

            blank_pointer = 0
            while blank_pointer < len(blanks) and file_position > blanks[blank_pointer]:
                blank_position = blanks[blank_pointer]
                blank_list = map_analysis[blank_position]

                # Blanks are kept at the end of each list
                blank_block = blank_list.pop(-1)

                if file_block.length <= blank_block.length:
                    # replace the file with blanks
                    replacement_blank_block = FileEntry(content=".", length=file_block.length)

                    # reduce size of blank
                    blank_block.length = blank_block.length - file_block.length
                    # add the file and blank back to the list of values
                    blank_list.append(file_block)
                    blank_list.append(blank_block)

                    # put the list of entries back in the map
                    map_analysis[file_position] = [replacement_blank_block]

                    # add blanks to blanks and remove from blanks
                    blanks.append(file_position)
                    blanks.sort()

                    # Worth removing blank from list of blanks if no blanks left? saves iteration but leads to array fiddling

                    break
                blank_list.append(blank_block)
                blank_pointer = blank_pointer + 1
            file_pointer = file_pointer + 1
        return map_analysis

    @classmethod
    def decode_analysis(cls, map_analysis: dict[int, list[FileEntry]]) -> list[str]:
        blocks = []
        for key, values in map_analysis.items():
            for item in values:
                for i in range(item.length):
                    blocks.append(str(item.content))
        return blocks
