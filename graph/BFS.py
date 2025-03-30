# BFS
from collections import deque
from GraphClass.MyGraph import Graph

def BFS(graph, source):
    # initialize the queue
    Q = deque()
    graph.visited[source] = True
    print(f'visited {source}')
    
    # add vertex
    Q.append(source)

    while Q: # while the queue is not empty
        vertex = Q.popleft()

        # add other verticies to the queue
        for child in graph.getEdges(vertex):
            if not graph.visited[child]:
                graph.visited[child] = True
                print(f'visited {child}')
                Q.append(child)
    
def main():
    graph = Graph({
        "a": ["b", "c"],
        "b": ["a", "d", "e"],
        "c": ["a", "f"],
        "d": [],
        "e": ["f"],
        "f": [],
        "g": ["f"]
    })

    BFS(graph, "a")

if __name__ == "__main__":
    main()