import heapq

nodes = {
    "A": [["B", 10], ["C", 4]],
    "B": [["A", 10], ["C", 4], ["D", 6]],
    "C": [["A", 4], ["B", 4], ["E", 6]],
    "D": [["B", 6], ["E", 6], ["F", 4]],
    "E": [["C", 6], ["D", 6], ["G", 14]],
    "F": [["D", 4], ["G", 4]],
    "G": [],
}

hValue = {"A": 16, "B": 4, "C": 16, "D": 2, "E": 1, "F": 4, "G": 0}

start = "A"
end = "G"
visited = []
cost = {start: 0}
openL = [(0, start)]

while openL:
    current = heapq.heappop(openL)
    if current[1] == end:
        break
    visited.append(current[1])
    for node, weight in nodes[current[1]]:
        if node in visited:
            continue
        if node not in cost or cost[current[1]] + weight < cost[node]:
            cost[node] = cost[current[1]] + weight
            heapq.heappush(openL, (cost[node] + hValue[node], node))

path = []
node = end
while node != start:
    path.append(node)
    min_cost = float('inf')
    for next_node, weight in nodes[node]:
        if cost[next_node] + weight == cost[node]:
            node = next_node
            break
path.append(start)
path = path[::-1]

print("Lowest Cost of each Node")
for i in cost.keys():
    print(f"{i}: {cost[i]}")

print("\nPath")
print(" --> ".join(path))
