a = int(input('Masukkan Nilai A ='))
b = int(input('Masukkan Nilai B ='))
c = (a*b)/a
if c > 100 :
    d = c + a
else:
    d = c - a
e = (d*a)/c
if e > 75 :
    f = d - e
elif e > 50 :
    f = d * a
else:
    f = d - b
print('Hasil Nilai C = ',c)
print('Hasil Nilai D = ',d )
print('Hasil Nilai E = ',e)
print('Hasil Nilai F = ',f)

