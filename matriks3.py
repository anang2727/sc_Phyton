a = [[2,0],[1,2]]
b = [[2,2,0],[1,1,2]]
c = [[0,0,0],[0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k]*b[k][j]
# Tampilkan matriks c
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j], end=' ')
    print()