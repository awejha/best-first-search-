from collections import deque

class Graph:
    

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
             'A': 9,
             'B': 10,
             'C': 13,
             'D': 9,
             'E': 17,
             'F': 4,
             'G': 0,
             'H': 9,
             'I': 11,
             'J': 2,
             'K': 5,
             'L': 14,
             'M': 4,
             'N': 6,
             'O': 11,
             'P': 4,
             'Q': 4,
             'R': 6,
             'S': 12
            }

        return (H[n], n)

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # Printing open and closed lists
            print(f"Open List: {open_list}")
            print(f"Closed List: {closed_list}")

            for v in open_list:
                if n is None or (g[v] + self.h(v)[0], v) < (g[n] + self.h(n)[0], n):
                    n = v;

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found:', reconst_path)
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                    print(f"Inspecting node {m}")

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# Test your modified A* algorithm
adjacency_list = {
    'S': [('C', 6), ('H', 16), ('K', 16), ('I', 6)],
    'A': [('B', 4), ('D', 20), ('C', 16)],
    'B': [('A', 4), ('F', 8)],
    'C': [('A', 16), ('D', 6), ('H', 6), ('S', 6)],
    'D': [('A', 20), ('C', 6), ('F', 4), ('H', 6)],
    'E': [('I', 24), ('L', 6)],
    'F': [('B', 8), ('D', 4), ('H', 16), ('J', 6)],
    'G': [('J', 4), ('M', 6), ('P', 6), ('Q', 10)],
    'H': [('F', 16), ('D', 6), ('C', 6), ('S', 16), ('K', 6)],
    'I': [('E', 24), ('L', 24), ('O', 24), ('N', 10), ('S', 6)],
    'J': [('M', 6), ('F', 6), ('G', 4)],
    'K': [('S', 16), ('N', 16), ('H', 6)],
    'L': [('I', 24), ('E', 6), ('O', 6)],
    'M': [('J', 6), ('P', 6), ('G', 6)],
    'N': [('I', 10), ('K', 16), ('R', 6), ('O', 16)],
    'O': [('N', 16), ('I', 24), ('L', 6)],
    'P': [('M', 6), ('G', 6), ('Q', 6)],
    'Q': [('P', 6), ('G', 10), ('R', 4)],
    'R': [('Q', 4), ('N', 6)]    
}

graph = Graph(adjacency_list)
graph.a_star_algorithm('S', 'G')
