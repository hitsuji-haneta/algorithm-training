maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    maze[x][y] = 2

    for i in range(len(dir)):
        j = (d + i - 1) % len(dir)
        xAfterTurn = x + dir[j][0]
        yAfterTurn = y + dir[j][1]
        if maze[xAfterTurn][yAfterTurn] < 2:
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[xAfterTurn][yAfterTurn] == 2:
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break

print(depth)
