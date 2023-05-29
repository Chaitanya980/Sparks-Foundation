## Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
arr=['5','3','7','8','4','2']
visited = []# Set to keep track of visited nodes of graph.

def DFS(node, graph):
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            DFS(child, graph)
    return visited


def BFS(node, graph):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        for child in graph[m]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
    return visited


def clearVisited(visited):
    while visited:
        visited.pop()



def menu():
    flag = True
    while (flag):
        clearVisited(visited)
        print("1] DFS\n 2] BFS\n 3] exit")
        choice = input("Enter choice: ")
        if choice == '1':
            node = input("Enter the starting node: ")
            if node in arr:
                print("Graph sequence DFS: ", DFS(node, graph))
            else:
                print("Wrong Input.!Try again.")
        elif choice == '2':
            node = input("Enter the starting node: ")
            if node in arr:
                print("Graph sequence BFS: ", BFS(node, graph))
            else:
                print("Wrong Input.!Try again.")
        elif choice == '3':
            print('Thank You')
            flag = False
        else:
            print("Wrong Input.!Try again.")


menu()