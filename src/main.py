from graph import Graph
from search_algorithms import bfs, dfs, a_star
from clustering import cluster_deliveries


# Heurística simples para o A*
def heuristic(node, goal):
    return abs(ord(goal) - ord(node))


def main():
    # Criando o grafo da cidade
    city = Graph()

    city.add_edge('A', 'B', 2)
    city.add_edge('A', 'C', 4)
    city.add_edge('B', 'D', 3)
    city.add_edge('C', 'D', 1)
    city.add_edge('D', 'E', 2)

    print("Resultado dos algoritmos de busca:\n")

    print("BFS:", bfs(city, 'A', 'E'))
    print("DFS:", dfs(city, 'A', 'E'))
    print("A* :", a_star(city, 'A', 'E', heuristic))

    print("\nAplicando clustering nas entregas:\n")

    clusters = cluster_deliveries('data/entregas.csv', n_clusters=2)
    print(clusters)


if _name_ == "_main_":
    main()
