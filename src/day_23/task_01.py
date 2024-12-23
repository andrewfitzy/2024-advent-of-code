class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        lan_connections: dict[str, set[str]] = {}
        for line in file_content:
            computers = line.split("-")

            connected_computers = lan_connections.get(computers[0], set())
            connected_computers.add(computers[1])
            lan_connections[computers[0]] = connected_computers

            connected_computers = lan_connections.get(computers[1], set())
            connected_computers.add(computers[0])
            lan_connections[computers[1]] = connected_computers

        connection_triples = set()
        for key, values in lan_connections.items():
            if not key.startswith("t"):
                continue
            for value in values:
                send_degree_connections = lan_connections[value]

                common_computers = values.intersection(send_degree_connections)

                for common_computer in common_computers:
                    connection_list = [key, value, common_computer]
                    connection_list.sort()

                    connection_triple = tuple(connection_list)
                    connection_triples.add(connection_triple)

        return len(connection_triples)
