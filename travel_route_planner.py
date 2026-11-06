import json
import heapq

# Colors
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"


class Graph:
    """Graph data structure using adjacency list"""

    def __init__(self):
        self.graph = {}

    def add_location(self, name):
        """Add a new location/node"""
        if name not in self.graph:
            self.graph[name] = []
            print(f"{GREEN}Location '{name}' added successfully!{RESET}")
        else:
            print(f"{YELLOW}Location '{name}' already exists.{RESET}")

    def add_road(self, start, end, distance):
        """Add a bidirectional road/edge"""
        if start not in self.graph or end not in self.graph:
            print(f"{RED}Error: One or both locations not found.{RESET}")
            return

        for neighbor, _ in self.graph[start]:
            if neighbor == end:
                print(f"{YELLOW}Road already exists between {start} and {end}.{RESET}")
                return

        self.graph[start].append((end, distance))
        self.graph[end].append((start, distance))

        print(
            f"{GREEN}Road added between {start} and {end} ({distance} units).{RESET}"
        )

    def shortest_path(self, start, end):
        """Dijkstra's Algorithm"""

        if start not in self.graph or end not in self.graph:
            return None, float("inf")

        if start == end:
            return [start], 0

        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0

        pq = [(0, start)]
        previous = {node: None for node in self.graph}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        if distances[end] == float("inf"):
            return None, float("inf")

        path = []
        node = end

        while node:
            path.insert(0, node)
            node = previous[node]

        return path, distances[end]

    def show_graph(self):
        """Display all locations and connections"""

        if not self.graph:
            print(f"{YELLOW}No locations available.{RESET}")
            return

        print(f"{BOLD}Graph Connections:{RESET}")

        for loc, neighbors in self.graph.items():
            connections = ", ".join(
                [f"{neighbor}({distance})" for neighbor, distance in neighbors]
            )
            print(
                f"{CYAN}{loc}:{RESET} "
                f"{connections if connections else 'No connections'}"
            )

    def save(self, filename="routes.json"):
        with open(filename, "w") as f:
            json.dump(self.graph, f)

        print(f"{CYAN}Data saved to {filename}{RESET}")

    def load(self, filename="routes.json"):
        try:
            with open(filename, "r") as f:
                self.graph = json.load(f)

            print(f"{CYAN}Data loaded from {filename}{RESET}")

        except FileNotFoundError:
            self.graph = {}
            print(f"{YELLOW}No saved data found. Starting fresh.{RESET}")


def get_valid_number(prompt):
    """Ensure valid float input"""

    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        try:
            return float(value)

        except ValueError:
            print(f"{RED}Invalid number. Try again.{RESET}")


def main():
    g = Graph()
    g.load()

    while True:
        print(f"\n{BOLD}--- Travel Route Planner ---{RESET}")
        print("1. Add Location")
        print("2. Add Road")
        print("3. Find Shortest Path")
        print("4. List Locations")
        print("5. Show Graph")
        print("6. Save Data")
        print("7. Load Data")
        print("0. Exit")

        choice = input(f"{CYAN}Enter choice: {RESET}").strip()

        # ADD LOCATION
        if choice == "1":
            print(
                f"{CYAN}Enter locations "
                f"(type 'exit' to return to menu){RESET}"
            )

            while True:
                name = input("Enter location name: ").strip()

                if name.lower() == "exit":
                    break

                if name:
                    g.add_location(name)
                else:
                    print(
                        f"{RED}Location name cannot be empty.{RESET}"
                    )

        # ADD ROAD
        elif choice == "2":
            print(
                f"{CYAN}Add roads "
                f"(type 'exit' to return to menu){RESET}"
            )

            while True:
                start = input("Enter start location: ").strip()

                if start.lower() == "exit":
                    break

                end = input("Enter end location: ").strip()

                if end.lower() == "exit":
                    break

                distance = get_valid_number(
                    "Enter distance (or 'exit'): "
                )

                if distance is None:
                    break

                g.add_road(start, end, distance)

        # SHORTEST PATH
        elif choice == "3":
            start = input(
                "Enter start location (or 'exit'): "
            ).strip()

            if start.lower() == "exit":
                continue

            end = input(
                "Enter destination location (or 'exit'): "
            ).strip()

            if end.lower() == "exit":
                continue

            path, dist = g.shortest_path(start, end)

            if path:
                print(
                    f"{GREEN}Shortest Path:{RESET} "
                    f"{' -> '.join(path)}"
                )
                print(
                    f"{CYAN}Total Distance:{RESET} {dist}"
                )
            else:
                print(
                    f"{RED}No path found between "
                    f"the given locations.{RESET}"
                )

        # LIST LOCATIONS
        elif choice == "4":
            if not g.graph:
                print(
                    f"{YELLOW}No locations available.{RESET}"
                )
            else:
                print(f"{BOLD}Locations:{RESET}")

                for loc in g.graph:
                    print(f" - {loc}")

        # SHOW GRAPH
        elif choice == "5":
            g.show_graph()

        # SAVE
        elif choice == "6":
            g.save()

        # LOAD
        elif choice == "7":
            g.load()

        # EXIT PROGRAM
        elif choice == "0":
            g.save()
            print(
                f"{GREEN}Exiting Travel Route Planner. "
                f"Goodbye!{RESET}"
            )
            break

        else:
            print(
                f"{RED}Invalid choice. Try again.{RESET}"
            )


if __name__ == "__main__":
    main()
