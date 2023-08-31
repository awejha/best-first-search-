import heapq

class Node:
    def __init__(self, id, heuristic):
        self.id = id
        self.heuristic = heuristic
        self.neighbors = []
        self.visited = False

class Edge:
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost

def gbs(start, target):
    queue = [(start.heuristic, start)]
    
    while queue:
        _, current_node = heapq.heappop(queue)
        print(f"Inspecting node: {current_node.id}")  # Print the current node
        
        if current_node == target:
            return current_node
        
        current_node.visited = True
        
        for edge in current_node.neighbors:
            neighbor = edge.target
            
            if not neighbor.visited:
                heapq.heappush(queue, (neighbor.heuristic, neighbor))
    
    return None

# Creating nodes with heuristic values
nodeA = Node("A", 150)
nodeB = Node("B", 140)
nodeF = Node("F", 130)
nodeS = Node("S", 130.1)
# Implenting tie-breaker between F and S,
# since actually h(F) = h(S) = 130, 
# but we want alphabetical priority be given to F over S,  
# so that h(S) = h(F) + ɛ for some infinitesimal ɛ
nodeC = Node("C", 100)
nodeD = Node("D", 100.1)
nodeH = Node("H", 100.2)
nodeE = Node("E", 90)
nodeK = Node("K", 90.1)
nodeM = Node("M", 90.2)
nodeI = Node("I", 80)
nodeJ = Node("J", 60)
nodeN = Node("N", 50)
nodeL = Node("L", 40.1)
nodeO = Node("O", 40.2)
nodeG = Node("G", 0)

# Creating edges with costs
nodeS.neighbors = [Edge(nodeA, 6), Edge(nodeB, 5), Edge(nodeC, 3)]
nodeA.neighbors = [Edge(nodeS, 6), Edge(nodeC, 5), Edge(nodeD, 5), Edge(nodeH, 5)]
nodeB.neighbors = [Edge(nodeS, 5), Edge(nodeC, 4), Edge(nodeE, 5), Edge(nodeF, 5)]
nodeC.neighbors = [Edge(nodeS, 3), Edge(nodeA, 5), Edge(nodeB, 4), Edge(nodeE, 3)]
nodeD.neighbors = [Edge(nodeA, 5), Edge(nodeE, 3)]
nodeH.neighbors = [Edge(nodeA, 5), Edge(nodeJ, 4), Edge(nodeN, 5)]
nodeE.neighbors = [Edge(nodeC, 3), Edge(nodeB, 5), Edge(nodeD, 3)]
nodeF.neighbors = [Edge(nodeB, 5), Edge(nodeI, 5), Edge(nodeK, 4), Edge(nodeM, 6)]
nodeJ.neighbors = [Edge(nodeI, 4), Edge(nodeH, 4), Edge(nodeN, 5)]
nodeN.neighbors = [Edge(nodeH, 5), Edge(nodeJ, 5), Edge(nodeG, 5)]
nodeI.neighbors = [Edge(nodeF, 5), Edge(nodeJ, 4), Edge(nodeL, 4)]
nodeK.neighbors = [Edge(nodeM, 4), Edge(nodeL, 5), Edge(nodeF, 4)]
nodeM.neighbors = [Edge(nodeF, 6), Edge(nodeK, 4), Edge(nodeO, 5)]
nodeG.neighbors = [Edge(nodeL, 4), Edge(nodeO, 4), Edge(nodeN, 5)]
nodeL.neighbors = [Edge(nodeI, 4), Edge(nodeK, 5), Edge(nodeG, 4), Edge(nodeO, 4)]
nodeO.neighbors = [Edge(nodeM, 5), Edge(nodeL, 4), Edge(nodeG, 4)]

# Call the function
result = gbs(nodeS, nodeG)

if result is not None:
    print(f"Path found! Target node is {result.id}")
else:
    print("Path not found. Failure.")
