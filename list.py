# a = [4,1,2,5,3,6]
# tot = 0
# for i in a:
#     tot=tot+i
# rata =tot/len(a)
# print("Total =",tot)
# print('Rata =',rata)

# a = [[2,1],[4,2]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print(a[i][j], end=' ')
#     print()

a =[[4,3,6],[1,4,0]]
b =[[3,0,2],[1,4,1]]
c =[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
for i in range(len(a)):
    for j in range(len(a[0])):
        print(c[i][j],end=' ')
    print()