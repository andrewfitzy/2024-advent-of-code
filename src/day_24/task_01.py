class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        process_inputs = True
        inputs = {}
        connections = {}
        for line in file_content:
            if len(line) == 0:
                process_inputs = False
                continue

            if process_inputs:
                input_parts = line.split(": ")
                inputs[input_parts[0]] = int(input_parts[1])
                continue

            input_parts = line.split(" ")
            operation = (input_parts[0], input_parts[1], input_parts[2])
            connections[input_parts[4]] = operation
            if input_parts[4] not in inputs:
                inputs[input_parts[4]] = -1

        output = cls.process(inputs=inputs, connections=connections)

        result = cls.convert_output_to_result(output)
        return result

    @classmethod
    def process(cls, inputs: dict[str, int], connections: dict[str, tuple[str, str, str]]) -> dict[str, int]:
        processing_inputs = dict(inputs)
        processing_connections = dict(connections)

        complete = False
        while not complete:
            complete = True
            for input, input_value in processing_inputs.items():
                if input_value == -1:
                    complete = False
                    left, operation, right = processing_connections[input]
                    if processing_inputs[left] > -1 and processing_inputs[right] > -1:
                        value = cls.get_value(
                            left=processing_inputs[left], operation=operation, right=processing_inputs[right]
                        )
                        processing_inputs[input] = value

        return processing_inputs

    @classmethod
    def get_value(cls, left: int, operation: str, right: int) -> int:
        if operation == "AND":
            return left & right
        if operation == "OR":
            return left | right
        return left ^ right

    @classmethod
    def convert_output_to_result(cls, output: dict[str, int]) -> int:
        z_registers = []
        # get all the zs here
        for key in output:
            if key.startswith("z"):
                z_registers.append(key)

        z_registers.sort()
        z_registers.reverse()

        value = []
        for register in z_registers:
            value.append(str(output[register]))
        value_str = "".join(value)
        value_dec = int(value_str, 2)
        return value_dec
