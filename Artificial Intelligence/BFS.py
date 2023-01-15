def main():

    start = input('Enter starting node: ')
    goal = input('Enter goal node: ')

    graph = {
        'a' : ['b','c','d'],
        'b' : ['e', 'f'],
        'c' : ['g','h'],
        'd' : ['i'],
        'e' : ['j','k'],
        'f' : [],
        'g' : ['l'],
        'h' : [],
        'i' : ['m'],
        'j' : [],
        'k' : ['n'],
        'l' : [],
        'm' : [],
        'n' : []
    }

    bfs(graph, start, goal)

def bfs(graph, start, goal):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        current_node = queue.pop(0)

        if current_node == goal:
            print (current_node)
            break
        print(current_node, end='->')

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
main()