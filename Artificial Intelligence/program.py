def aStarAlgoritm(start, stop):
    open_set = set(start)
    closed_set = set()
    g = {}
    parents = {}

    g[start] = 0
    parents[start] = start

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None  or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        if n == stop or Graph_nodes[n] == None:
            pass

        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] - g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
            
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start)
                path.reverse()

                print('Path found: {}'.format(path))
                return path


            open_set.remove(n)
            closed_set.add(n)
        
        print('path does not exist')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 16,
        'B': 4,
        'C': 16,
        'D': 2,
        'E': 1,
        'F': 4,

    }

    return H_dist[n]

Graph_nodes = {
    'A': [('B',10), ('C',4)],
    'B': [('D',6), ('C',4)],
    'C': [('B',4), ('E',6)],
    'D': [('E',6), ('F',4)],
    'E': [('D',6), ('G',14)],
    'F': [('G',4)],
}
aStarAlgoritm('A', 'G')