from typing import List

def findPoints(point: List) -> List:
    valid_points = []
    movements = [[1,2], [2,1], [-1,2], [2,-1], [1,-2], [-2,1], [-1,-2], [-2,-1]]
    x, y = point[0], point[1]
    for pair in movements:
        new_x = x + pair[0]
        new_y = y + pair[1]
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            valid_points.append([new_x, new_y])
    
    return valid_points

def printBoard(board):
    print("Board:")
    for x in board:
        s = ""
        for y in x:
            s += str(y) + " "
        print(s)

def solve(start: List, end: List):
    
    if start == end:
        return 0

    visited = [start]
    
    board = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    while visited:
        current = visited.pop(0)
        #print("Point: ", current)
        x, y = current[0], current[1]
        move = board[x][y]
        squares = findPoints(current)
        #print("Visited: ", visited)
        #print("Valid Squares: ", squares)
        
        for point in squares:
            if point == end:
                return move + 1
            if board[point[0]][point[1]] == 0:
                visited.append(point)
                board[point[0]][point[1]] = move + 1
    return -1
                
start = [int(c) - 1 for c in input().split(" ")]
end = [int(c) - 1 for c in input().split(" ")]

print(solve(start, end))