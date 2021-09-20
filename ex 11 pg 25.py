n = int(input('Dați numărul de elemente din vector:'))
a = []
print('Introduceți ', n, ' elemente pentru vectorul creat:')
for i in range(0, n):
    x = int(input('Dați elementul: '))
    a.extend([x])
print(a)
print('a)  Afişează pe ecran componentele tabloului la un interval de 5 poziţii: ', *a[0:5])
print('b)  Afişează pe ecran numerele în ordinea inversă a introducerii în calculator: ', *a[::-1])
b = sorted(a)
b.sort(reverse=True)
print('c)Sortează componentele tabloului în ordine descrescătoare:', *b)
c = []
for i in range(0, len(a)):
    if a[i] % 3 == 0:
        y = a[j]
        c.extend([y])
print('d)  Afişează pe ecran doar componentele pare: ', *c)
print('e)  Afişează pe ecran media aritmetică a componentelor pare:', sum(c) / len(c))
d = []
for k in range(0, len(a)):
    if a[k] %  != 0:
        y = a[k]
        d.extend([y])
print('f)  Afişează pe ecran doar componentele impare: ',*e)
x, y = eval(input('Dati valorile x, y: '))
f = []
for l in a:
    if (l>x) and (l % y != 0):
     e.extend([l])
print('g)  Afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y:', *f)
g = []
for z in a:
 if (z > x) and (z < y):
 g.extend([z])
print('h)  Afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y: ', *g)
h = []
for v in a:
    if (v < 0) and (v % 2 != 0):
      h.extend([a.index(v)])
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative: ', *h)
i = []
for b in a: 
    if ((abs(b) // 10) < 10) and ((abs(b) // 10) > 0):
        i.extend([a.index(b)])
print('j)  afişează pe ecran poziţiile (indicii)componentelor ce conţin doar două cifre semnificative: ', *j)
a1 = a.copy()
a1[0] = min(a)
