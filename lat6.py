a = int(input('Masukkan A='))
b = int(input('Masukkan B='))
c = (a*b)/(a+b)
if c > 50:
    d =c-b
else:
    d=c*b
e = d+c
if e > 75:
    f=d+e
else:
    f=d*e
print('Hasil Nilai C', c)
print('Hasil Nilai D', d)
print('Hasil Nilai E', e)
print('Hasil Nilai F', f)
