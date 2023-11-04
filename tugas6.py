a = int(input('Masukkan Nilai A ='))
b = int(input('Masukkan Nilai B ='))
c = (a*b)/(a+b)
if c > 100 :
    d = c - a
elif c > 75:
    d = c * b
else:
    d = (c-a)/b
e = (d+a)*b
if e  > 75 :
    f = d + c
elif e > 50 :
    f = d + e
else:
    f = d + d
g = (d+e)/f
print('Hasil Nilai C =', c)
print('Hasil Nilai D =', d)
print('Hasil Nilai E =', e)
print('Hasil Nilai F =', f)
print('Hasil Nilai G =', g)

