def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[0] * n for _ in range(n)]
    for fare in fares:
        p1, p2, cost = fare
        graph[p1 - 1][p2 - 1] = cost
        graph[p2 - 1][p1 - 1] = cost
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                graph[i][j] = INF
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    def cost(start, end):
        return graph[start - 1][end - 1]

    min_cost = 40000002
    for i in range(1, n + 1):
        min_cost = min(min_cost, cost(s, i) + cost(i, a) + cost(i, b))
    return min_cost
