def is_valid(v, pos, path, graph):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return True
    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False


def hamiltonian(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start from vertex 0

    if not hamiltonian_util(graph, path, 1):
        print("No Hamiltonian path exists")
        return False

    print("Hamiltonian path:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])  # Print the starting vertex again to complete the cycle

    return True

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian(graph)
