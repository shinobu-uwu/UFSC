x = [-1, 0, 1]
y = [4, 1, -1]
n = len(x)
v = [[0] * 3 for x in range(n)]
for i in range(n):
    for j in range(n):
        v[i][j] = x[i] ** j
print(v)
