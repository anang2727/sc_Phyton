a = 10
b = int(input('Masukkan Nilai B ='))
e=(a-b)
c = (a*b)/e if e!=0 else 0
if c > 150:
    d = c-a
elif c > 100:
    d = c*b
else:
    d =c+a
print('Hasil Nilai C = ',c)
print('Hasil Nilai D = ',d)

