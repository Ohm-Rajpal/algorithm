# DFS
from GraphClass.MyGraph import Graph

def DFS(graph, explore):
    for vertex in graph.getVertices():
        if not graph.visited[vertex]:
            explore(graph, vertex)

def explore_recursive(graph, vertex):    
    graph.visited[vertex] = True
    print(f'visited vertex {vertex}')  # Print when marking as visited
    for child in graph.getEdges(vertex):
        if not graph.visited[child]:
            explore_recursive(graph, child)

def explore_iterative(graph, vertex):
    # iterative method uses a stack
    my_stack = [vertex]

    while my_stack:
        temp_node = my_stack.pop()
        # if haven't explored the current node, explore the edges
        if not graph.visited[temp_node]:
            graph.visited[temp_node] = True
            print(f'visited vertex {temp_node}')  # Print when marking as visited

            for child in sorted(graph.getEdges(temp_node), reverse=True):
                if not graph.visited[child]:
                    my_stack.append(child)

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

    print('recursive:')
    DFS(graph, explore_recursive)
    print()
    # reset visited
    graph.visited = {vertex : False for vertex in graph.getVertices()}

    print('iterative:')
    DFS(graph, explore_iterative)
    print()

if __name__ == "__main__":
    main()