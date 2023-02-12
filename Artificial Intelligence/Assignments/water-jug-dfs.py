root = [0,0]
openL = []
closeL = []
end = [2,0]
maps = {}
openL.insert(0,root)
tree = []
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
    if end == [five,four]:
        break
    if five < 5:
        five = 5
        if [five,four] not in closeL and [five,four] not in openL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if four < 4:
        four = 4
        if [five,four] not in closeL and [five,four] not in openL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if five > 0:
        five = 0
        if [five,four] not in closeL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if four > 0:
        four = 0
        if [five,four] not in closeL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if five > 0 and four < 4:
        if four+five > 4:
            temp = 4 - four
            five-=temp
            four+=temp
        else:
            four+=five
            five = 0
        if [five,four] not in closeL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]
    if four > 0 and five < 5:
        if four+five > 5:
            temp = 5 - five
            four-=temp
            five+=temp
        else:
            five+=four
            four = 0
            
        if [five,four] not in closeL:
           openL.insert(0,[five,four])
           lis.append([five,four])
        tree[-1].append([five,four])
        five = node[0]
        four = node[1]

for i in tree:
    print(i)
i = 0
while True:
    if closeL[i+1] == root:break
    if closeL[i] in maps[str(closeL[i+1])]:
        i+=1
    else:
        closeL.pop(i+1)
closeL.reverse()
print()
print(closeL)
