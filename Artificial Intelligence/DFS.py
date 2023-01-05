graph = {
  'a' : ['e','b','g'],
  'b' : ['a', 'h','g','f','c'],
  'c' : ['b','h','d'],
  'd' : ['c','e'],
  'e' : ['a','d','f'],
  'f' : ['e','b'],
  'g' : ['a','b'],
  'h' : ['b','c']
}
start = input("Enter Start Node:")
goal = input("Enter Goal Node:")
visited = set() 
def dfs(visited, graph, node, goal):  
        if node not in visited:
            print (node)
            visited.add(node)
            if(node == goal):
                print("Reached")
            else:
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour, goal)
            

print("Following is the Path")
dfs(visited, graph, start, goal)