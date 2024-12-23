class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> str:
        lan_connections: dict[str, set[str]] = {}
        for line in file_content:
            computers = line.split("-")

            connected_computers = lan_connections.get(computers[0], set())
            connected_computers.add(computers[1])
            lan_connections[computers[0]] = connected_computers

            connected_computers = lan_connections.get(computers[1], set())
            connected_computers.add(computers[0])
            lan_connections[computers[1]] = connected_computers

        # Keep a count of all of the appearances of a set of intersections
        network_appearances: dict[tuple[str, ...], int] = {}
        for computer in lan_connections.keys():
            networks = cls.get_network(computer, lan_connections)
            for network in networks:
                appearance_count = network_appearances.get(network, 0)
                appearance_count = appearance_count + networks[network]
                network_appearances[network] = appearance_count

        # work out which intersection has been seen most often
        biggest_network: tuple[str, ...] = ("", "")
        biggest_seen_count = 0
        for network_nodes, count in network_appearances.items():
            if count > biggest_seen_count:
                biggest_network = network_nodes
                biggest_seen_count = count

        # Manipulate the network into a sorted list and join into a string
        biggest_network_list = list(biggest_network)
        biggest_network_list.sort()
        biggest_network_str = ",".join(biggest_network_list)
        return biggest_network_str

    @classmethod
    def get_network(cls, start_computer: str, map: dict[str, set[str]]) -> dict[tuple[str, ...], int]:
        """
        Works by getting the connections to a start computer, then getting the connections (2nd level) to
        each one of those connections and then getting the intersection of second level and current connections.

        For example, if the computer is 'de' we would get the connections:
        'de': {'cg', 'co', 'ta', 'ka'},

        this would be combined into a "network" of:
        {'de', 'cg', 'co', 'ta', 'ka'}

        We then get each of the second level connections and get the intersection with network:
        'cg': ['de', 'tb', 'yn', 'aq'], --> 'cg', 'de'
        'co': ['ka', 'ta', 'de', 'tc'], --> 'co', 'ka', 'ta', 'de'
        'ta': ['co', 'ka', 'de', 'kh'], --> 'ta', 'co', 'ka', 'de'
        'ka': ['co', 'tb', 'ta', 'de'], --> 'ka', 'co', 'ta', 'de'

        Finally sorting the intersections, storing in a tuple and counting the number of occurrences, returning in a dict like:

        {
          ('co', 'de', 'ka', 'ta'): 3,
          ('cg', 'de'): 1
        }

        The calling function can then sum up all the times that the same LAN setup is seen and this should give the most most connected computers.
        """

        # Keep track of appearances of intersections
        appearances: dict[tuple[str, ...], int] = {}

        connected_computers = set(map[start_computer])

        network = set(map[start_computer])
        network.add(start_computer)

        for computer in connected_computers:
            second_level_connections = set(map[computer])
            second_level_connections.add(computer)

            intersection_list = list(network.intersection(second_level_connections))
            intersection_list.sort()
            intersections = tuple(intersection_list)
            appearance_count = appearances.get(intersections, 0)
            appearance_count = appearance_count + 1
            appearances[intersections] = appearance_count

        return appearances
