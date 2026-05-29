from collections import deque
maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", "G", "."]
]

def print_maze(maze):
    for row in maze:
        for cell in row:

            if cell == "#":
                print("⬛", end=" ")

            elif cell == ".":
                print("⬜", end=" ")

            elif cell == "*":
                print("🟩", end=" ")

            elif cell == "S":
                print("🤖", end=" ")

            elif cell == "G":
                print("🏁", end=" ")

        print()
            
def find_position(maze, target):
    for row_index, row  in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == target:
                return row_index, col_index
def get_possible_moves(maze, row, col):
    moves = []
    if col + 1 < len(maze[0]) and maze[row][col + 1] != "#":
        moves.append("right")
    if col - 1 >= 0 and maze [row][col - 1] != "#":
        moves.append("left")
    if row + 1 < len (maze) and maze[row + 1][col] != "#":
        moves.append("down")
    if row - 1 >= 0 and maze[row - 1][col] != "#":
        moves.append("up")
    return moves  
def bfs(maze, start, goal):
    queue = deque([start])
    visited = set()
    parent = {}
    while queue:
        current = queue.popleft()
        print("Current =", current, "Goal =", goal)
        if current == goal:
            print("Goal found!")
            print("Goal =", goal)
            print("Parent of goal =", parent.get(goal))
            path = []
            current_node = goal
            while current_node != start:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            print("Shortest path:")
            print(path)
            for row, col in path:
                if maze[row][col] != "S" and maze[row][col] != "G":
                    maze[row][col] = "*"
            print()
            print("Solved Maze:")
            print_maze(maze)
            return
        if current in visited:
            continue
        visited.add(current)
        print("Visiting:", current)
        row, col = current
        moves = get_possible_moves(maze, row, col)
        if "right" in moves:
            next_pos = (row, col + 1)
        if next_pos not in parent:
            queue.append(next_pos)
            parent[next_pos] = current
        if "left" in moves:
            next_pos = (row, col - 1)
        if next_pos not in parent:
            queue.append(next_pos)
            parent[next_pos] = current
        if "down" in moves:
            next_pos = (row + 1, col)
        if next_pos not in parent:
            queue.append(next_pos)
            parent[next_pos] = current
        if "up" in moves:
            next_pos = (row - 1, col)
        if next_pos not in parent:
            queue.append(next_pos)
            parent[next_pos] = current             
print_maze(maze)
start = find_position(maze, "S")
goal = find_position(maze, "G")
bfs(maze, start, goal)

