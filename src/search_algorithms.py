import heapq

def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        node, path = queue.pop(0)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get_neighbors(node):
                queue.append((neighbor, path + [neighbor]))

    return None


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get_neighbors(node):
                stack.append((neighbor, path + [neighbor]))

    return None


def a_star(graph, start, goal, heuristic):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph.get_neighbors(node):
                new_cost = cost + weight + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path + [neighbor])
                )

    return None
