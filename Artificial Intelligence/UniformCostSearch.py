def uniform_cost_search(goal, start):
	
	global graph,cost
	answer = []

	queue = []

	for i in range(len(goal)):
		answer.append(10**8)

	queue.append([0, start])

	visited = {}

	count = 0

	while (len(queue) > 0):

		queue = sorted(queue)
		p = queue[-1]

		del queue[-1]

		p[0] *= -1

		if (p[1] in goal):

			index = goal.index(p[1])

			if (answer[index] == 10**8):
				count += 1

			
			if (answer[index] > p[0]):
				answer[index] = p[0]

			
			del queue[-1]

			queue = sorted(queue)
			if (count == len(goal)):
				return answer

		
		if (p[1] not in visited):
			for i in range(len(graph[p[1]])):

				queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

	
		visited[p[1]] = 1

	return answer

if __name__ == '__main__':
	
	graph,cost = listToString([[] for i in range(8)]),{}

	graph['a'].append('b')
	graph['a'].append('c')
	graph['b'].append('g')
	graph['c'].append('d')
	graph['c'].append('e')
	graph['d'].append('g')
	graph['e'].append('g')
	
	

	cost[('a', 'b')] = 4
	cost[('a', 'c')] = 1
	cost[('b', 'g')] = 13
	cost[('c', 'd')] = 3
	cost[('c', 'e')] = 1
	cost[('d', 'g')] = 2
	cost[('e', 'g')] = 4

	goal = []

	goal.append(g)

	answer = uniform_cost_search(goal, 'a')

	print("Minimum cost from a to g is = ",answer[0])
