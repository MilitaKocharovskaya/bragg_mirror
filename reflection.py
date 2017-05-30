import matplotlib.pyplot as plt

n = int(input())    #n - количество значений длин волн
m1, m2 = map(int(input().split()))    #m1, m2 - количество пар слоев
d = [[]*n]

s = open('refl.txt')
k = 0
for line in s.readlines():
    a = list(map(int, line.split()))
    d[k].append(a[0])   #длина волны
    d[k].append(a[1])   #показатель преломления SiO2
    d[k].append(a[2])   #показатель преломления TiO2
    k += 1
s.close()

for i in range(n):
    r1 = ((1 - (d[i][1]/d[i][2])^(2*m1))/(1 + (d[i][2]/d[i][1])^(2*m1)))^2
    d[i].append(r1)
    r2 = ((1 - (d[i][1]/d[i][2])^(2*m2))/(1 + (d[i][2]/d[i][1])^(2*m2)))^2
    d[i].append(r2)

x1 = []
y1 = []
for i in range(n):
    x1.append(d[i][0])
    y1.append(d[i][3])
x2 = []
y2 = []
for i in range(n):
    x2.append(d[i][0])
    y2.append(d[i][4])

plt.plot(x1, y1, x2, y2)
plt.plot(x1, y1, label = r'm1 слоев')
plt.plot(x2, y2, label = r'm2 слоев')
plt.xlabel(r'$длина волны, нм$')
plt.ylabel(r'$R$')
plt.title(r'$Зависимость коэффициента отражения от длины волны$')
#plt.axis([мин длина волны, макс длина волны, минР, максР])
plt.grid(True)
plt.show()

