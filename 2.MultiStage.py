def multistage_graph(graph, stages):
    n = len(graph)
    cost = [float('inf')] * n
    path = [0] * n

    cost[n-1] = 0

    for i in range(n-2, -1, -1):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] + cost[j] < cost[i]:
                cost[i] = graph[i][j] + cost[j]
                path[i] = j

    optimal_path = [0]
    current_stage = 0
    while current_stage < stages - 1:
        current_stage += 1
        optimal_path.append(path[current_stage])

    return optimal_path, cost[0]

graph = [
    [0, 1, 2, 5, 0, 0],
    [0, 0, 0, 0, 4, 11],
    [0, 0, 0, 0, 9, 5],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
stages = 6

optimal_path, min_cost = multistage_graph(graph, stages)
print("Optimal Path:", optimal_path)
print("Minimum Cost:", min_cost)
