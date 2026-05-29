import tkinter as tk
from collections import deque

window = tk.Tk()
window.title("Robot Maze Solver")
window.geometry("600x600")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", "G", "."]
]

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x1 = 100 + col * 60
            y1 = 100 + row * 60
            x2 = x1 + 60
            y2 = y1 + 60

            if maze[row][col] == "S":
                color = "green"
            elif maze[row][col] == "G":
                color = "red"
            elif maze[row][col] == "#":
                color = "black"
            else:
                color = "white"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def find_position(maze, target):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == target:
                return row, col

def get_neighbors(maze, row, col):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] != "#":
                neighbors.append((new_row, new_col))

    return neighbors

def bfs(maze, start, goal):
    queue = deque([start])
    visited = set()
    parent = {}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            current_node = goal

            while current_node != start:
                path.append(current_node)
                current_node = parent[current_node]

            path.append(start)
            path.reverse()
            return path

        if current in visited:
            continue

        visited.add(current)

        row, col = current

        for neighbor in get_neighbors(maze, row, col):
            if neighbor not in visited and neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = current

    return []

draw_maze()

start = find_position(maze, "S")
goal = find_position(maze, "G")
path = bfs(maze, start, goal)

robot = canvas.create_oval(110, 110, 150, 150, fill="yellow")

def move_robot():
    for row, col in path:
        x = col * 60
        y = row * 60

        if maze[row][col] != "S" and maze[row][col] != "G":
            x1 = 100 + col * 60
            y1 = 100 + row * 60
            x2 = x1 + 60
            y2 = y1 + 60

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="deepskyblue",
                outline="gray",
                tags="path"
            )

        canvas.coords(robot, 110 + x, 110 + y, 150 + x, 150 + y)
        canvas.tag_raise(robot)
        window.update()
        window.after(1000)

def reset_robot():
    canvas.delete("path")
    canvas.coords(robot, 110, 110, 150, 150)
    canvas.tag_raise(robot)

start_button = tk.Button(window, text="Start Robot", command=move_robot)
start_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_robot)
reset_button.pack()

window.mainloop()