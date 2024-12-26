class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        locks, keys = cls.get_locks_and_keys(file_content)

        pairs = 0
        for lock in locks:
            for key in keys:
                if cls.key_works_in_lock(lock, key):
                    pairs = pairs + 1

        return pairs

    @classmethod
    def get_locks_and_keys(cls, file_content: list[str]) -> tuple[list[list[list[str]]], list[list[list[str]]]]:
        keys = []  # ### at the bottom
        locks = []  # ### at the top
        buffer: list[list[str]] = []
        for row in file_content:
            if len(row) == 0:
                if buffer[0][0] == "#":
                    locks.append(buffer)
                else:
                    keys.append(buffer)
                buffer = []
                continue
            buffer.append(list(row))

        if buffer[0][0] == "#":
            locks.append(buffer)
        else:
            keys.append(buffer)

        return (locks, keys)

    @classmethod
    def key_works_in_lock(cls, lock: list[list[str]], key: list[list[str]]) -> bool:
        for lock_row_index in range(len(lock)):
            for lock_col_index in range(len(lock[0])):
                if (
                    lock[lock_row_index][lock_col_index] == "#"
                    and lock[lock_row_index][lock_col_index] == key[lock_row_index][lock_col_index]
                ):
                    return False
        return True
