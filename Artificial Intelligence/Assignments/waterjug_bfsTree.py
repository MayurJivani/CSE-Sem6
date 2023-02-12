root = [0,0]
openL = []
closeL = []
end = [2,0]
maps = {}
openL.append(root)
tree = []
goalPaths = []
rootPaths = []
while True:
    tree.append([])
    node = openL[0]
    closeL.insert(0,node)
    openL.pop(0)
    five = node[0]
    four = node[1]
    maps[str(node)] = []
    lis = maps[str(node)]
    tree[-1].append(node)
    tree[-1].append("------>")
    if five < 5:
        five = 5
        if [five,four] not in closeL and [five,four] not in openL:
           openL.append([five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if four < 4:
        four = 4
        if [five,four] not in closeL and [five,four] not in openL:
           openL.append([five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if five > 0 and four < 4:
        if four+five > 4:
            temp = 4 - four
            five -= temp
            four += temp
        else:
            four+=five
            five = 0
        if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if four > 0 and five < 5:
        if five+four > 5:
            temp = 5 - five
            four-=temp
            five+=temp
        else:
            five+=four
            four = 0
    if [five,four] not in closeL:
           openL.append([five,four])
           lis.append([five,four])
    tree[-1].append([five,four])
    five = node[0]
    four = node[1]
    if len(openL) == 0:
        break
goalIndex = 0
for i in tree:
    print(i)
    if end == i[0]:
        goalIndex = tree.index(i)
s = 0
while True:
    rootPaths.append(tree[s][0])
    goalPaths.insert(0,tree[goalIndex - s][0])
    if goalPaths[0] == rootPaths[-1]:
        break
    s+=1
finalPath = []
for i in rootPaths:
    if i not in finalPath:
        finalPath.append(i)
for i in goalPaths:
    if i not in finalPath:
        finalPath.append(i)
print()
print("Root Path: ",rootPaths)
print("Goal Path: ",goalPaths)
print("Total Path: ",finalPath)
finalPath.reverse()
i = 0
while True:
    try:
        if finalPath[i+1] == root:break
        if finalPath[i] in maps[str(finalPath[i+1])]:
            i+=1
        else:
            finalPath.pop(i+1)
    except:
        print("Solution Do Not Exist")
        exit()
finalPath.reverse()
print("Final Path: ",finalPath)
