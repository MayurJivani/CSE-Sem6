nodes = {
    "S": [["A", 5], ["B", 9], ["D", 6]],
    "A": [["B", 3], ["G1", 9]],
    "B": [["C", 1]],
    "C": [["G2", 5], ["F", 7], ["S", 6]],
    "D": [["C", 2], ["E", 2]],
    "E": [["G3", 7]],
    "G1": [],
    "F": [["D", 2], ["G3", 8]],
    "G3": [],
    "G2": [],
}
start = "S"
end = "G2"
visited = []
cost = {}
openL = []
maps = {}
for i in nodes.keys():
    li = []
    for j in nodes[i]:
        li.append(j[0])
    maps[i] = li
openL.append(["S",0])
cost[openL[0][0]] = 0
lastNode= openL[-1]
while True:
    lastNode = openL[0]
    l = nodes[openL[0][0]]
    visited.append(openL[0])
    openL.pop(0)
    flag = False
    for i in l:
        if i not in visited:
            if i[0] not in cost:
                flag = True
                cost[i[0]] = i[1] + lastNode[1]
                openL.append([i[0],cost[i[0]]])
            else:
                if cost[i[0]] > i[1] + lastNode[1]:
                    flag = True
                    for j in openL:
                        if j[0] == i[0]:
                            cost[i[0]] = i[1] + lastNode[1]
                            openL[openL.index(j)] = [i[0],cost[i[0]]]
    if not flag and len(l) != 0:
        visited.pop(-1)
    openL.sort(key=lambda i:i[1])
    if openL == []:break
visited.reverse()
while True:
    if visited[0][0] != end:
        visited.pop(0)
    else:
        break
i = 0
j = 1
while True:
    if visited[j][0] == start:break
    if visited[i][0] not in maps[visited[j][0]]:
        visited.remove(visited[j])
    else:
        i+=1
        j+=1
visited.reverse()
print("\nLowest Cost of each Node")
for i in cost.keys():
    print(f"{i}:{cost[i]}")
print("\nPath")
for i in visited[:-1]:
    print(i[0],end="--->")
print(visited[-1][0])

