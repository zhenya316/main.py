n, m = (10, 10)  # чтение размеров поля и числа мин
k = int(input())
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
import random
from random import randint
s = 0
while s < k:
    row = randint(0, n-1)
    col = randint(0, m-1)
    if a[row][col] == -1:
        s -= 1
        continue
    elif a[row][col] == 0:
        a[row][col] = -1
        s += 1              # расставляем мины
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end=' ')
        elif a[i][j] == 0:
            print('.', end=' ')
        else:
            print(a[i][j], end=' ')
    print()
a1 = a

def field_users(a1):
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                print('+', end=' ')
            elif a[i][j] == 0:
                print('+', end=' ')
            else:
                print('+', end=' ')
        print()
print(field_users(a1))


x, y = (int(i) - 1 for i in input().split())

def bfs(s):
    global a1
    a1[s] = 0
queue = [s]
while queue:
    if a[x][y] == -1:
        print('game over')
    elif a[x][y] == 0:
        v = queue.pop(0)
        a[x][y] = a[x][y]
    else:
        a[x][y]
    for w in a[v]:
        if a[x][y]  == 0:
            queue.append(w)