# Assignment #1
# 길찾기
import random
from collections import deque
from re import X

def makeGrid():
    logoLoc = [random.randint(0, vert - 1), random.randint(0, hor - 1)]
    grid[logoLoc[0]][logoLoc[1]] = 2
    for _1 in range(vert):
        for _2 in range(hor):
            if grid[_1][_2] != 2:
                grid[_1][_2] = random.randint(0,1)
    grid[0][0] = 0


def printGridInfo(x):
    print("0은 공간, 1은 벽, 2는 도착를 표시한다.\n지도:")
    for y in range(vert):
        print(grid[y])
    
    if x == -1:
        print("도착 불가")
        return -1
    else:
        print("거리: "+str(x))
        return 1


def BFS(x, y):
    q.append([x, y, 0])
    grid[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]
        dist = t[2]
        for i3 in range(4):
            tempX = tx + dx[i3]
            tempY = ty + dy[i3]
            if 0 <= tempX < hor and 0 <= tempY < vert:
                if grid[tempY][tempX] == 0:
                    q.append([tempX, tempY, dist + 1])
                    grid[tempY][tempX] = 1
                if grid[tempX][tempY] == 2:
                    return dist + 1
    return -1


def printTempGrid():
    for i in range(vert):
        tempLine = " ".join(tempGrid[i])
        print(tempLine)
    pass


hor = 8
vert = 8
tVal = -1
while True:
    grid = [[1 for _ in range(hor)]for _ in range(hor)]
    finLoc = [-1,-1]
    q = deque()
    q.clear()
    print(q)
    makeGrid()
    tVal = BFS(0,0)
    # printGridInfo(tVal)
    if tVal != -1:
        break
print(".은 모르는곳, O는 길, X는 벽으로 표시하고 현재 위치는 @으로 표현한다.... 로고를 찾아라!")
print("방향은 4가지가있다. UP, DOWN, LEFT, RIGHT")
tempGrid = [["." for i in range(hor)] for i2 in range(vert)]
tempGrid[0][0] = "@"
tempCoord  = [0, 0]
printTempGrid()
while True:
    direct = input("방향을 골라라: \n")
    d = [0, 0]
    if direct == "UP":
        d = [0, -1]
    elif direct == "DOWN":
        d = [0, 1]
    elif direct == "RIGHT":
        d = [1, 0]
    elif direct == "LEFT":
        d = [-1, 0]
    else:
        print("?????")
        continue
    if not (0 <= tempCoord[0] + d[1] <= vert and 0 <= tempCoord[1] + d[0] <= hor):
        print("바깥으로 가지마세요...")
        continue
    if grid[tempCoord[0] + d[1]][tempCoord[1] + d[0]] == 0:
        print("벽이 있네요...")
        tempGrid[tempCoord[0] + d[1]][tempCoord[1] + d[0]] = "X"
    elif grid[tempCoord[0] + d[1]][tempCoord[1] + d[0]] == 1:
        print("길이있어요!")
        tempGrid[tempCoord[0] + d[1]][tempCoord[1] + d[0]] = "@"
        tempGrid[tempCoord[0]][tempCoord[1]] = "O"
        tempCoord = [tempCoord[0] + d[1], tempCoord[1] + d[0]]
    elif grid[tempCoord[0] + d[1]][tempCoord[1] + d[0]] == 2:
        print("찾았어요!!!!!!")
        break
    printTempGrid()
    
