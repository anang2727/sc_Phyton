a = [[2, 4, 1], [1, 7, 2]]
b = [[3, 0, 7], [1, 1, 2]]
c = [[0, 0, 0], [0, 0, 0]]
d = [[0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j], end=" ")
    print()

for i in range(len(a)):
    for j in range(len(a[0])):
        d[i][j] = a[i][j] - b[i][j]
for i in range(len(d)):
    for j in range(len(d[0])):
        print(d[i][j], end=" ")
    print()
