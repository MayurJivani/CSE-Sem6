def manhattan_distance(puzzle, goal):
    distance = 0
    for i in range(9):
        x, y = divmod(i, 3)
        x_goal, y_goal = divmod(goal.index(puzzle[i]), 3)
        distance += abs(x - x_goal) + abs(y - y_goal)
    return distance

def a_star(start, goal):
    open_list = [(manhattan_distance(start, goal), start, [], 0)]
    closed_list = []

    while open_list:
        (f, puzzle, path, g) = min(open_list, key=lambda x: x[0] + x[3])
        open_list.remove((f, puzzle, path, g))
        closed_list.append((f, puzzle, path, g))

        if puzzle == goal:
            return (path, g)

        zero_index = puzzle.index(0)
        x, y = divmod(zero_index, 3)
        neighbors = [(x + i, y + j) for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for (x_neighbour, y_neighbour) in neighbors:
            if 0 <= x_neighbour < 3 and 0 <= y_neighbour < 3:
                puzzle_copy = puzzle.copy()
                index_neighbour = 3 * x_neighbour + y_neighbour
                puzzle_copy[zero_index], puzzle_copy[index_neighbour] = puzzle_copy[index_neighbour], puzzle_copy[zero_index]
                if (manhattan_distance(puzzle_copy, goal), puzzle_copy, path + [puzzle], g + 1) not in closed_list:
                    open_list.append((manhattan_distance(puzzle_copy, goal), puzzle_copy, path + [puzzle], g + 1))
    
    return None

start = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goal = [1, 2, 3, 4, 0, 5, 6, 7, 8]
result = a_star(start, goal)
if result:
    (path, cost) = result
    print("Path:")
    for puzzle in path:
        print("[{} {} {}]".format(*puzzle[:3]))
        print("[{} {} {}]".format(*puzzle[3:6]))
        print("[{} {} {}]".format(*puzzle[6:]))
        print()
    print("Total cost:", cost)
else:
    print("No solution found.")
