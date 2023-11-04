# If Else
a = int(input('Masukkan Nilai A ='))
b = int(input('Masukkan Nilai B ='))
c = int(input('Masukkan Nilai C ='))
d = (a*b)/c
if d > 100 :
    e = d-a
elif d > 75 :
    e = d + b
else:
    e=(d+c)/a
f = (e+a)/b
print('Hasil Nilai D =',d)
print('Hasil Nilai E =',e)
print('Hasil Nilai F =',f)