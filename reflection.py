import matplotlib.pyplot as plt

n = int(input())    #n - количество значений длин волн
m = int(input())    #m - количество пар слоев
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
    r = ((1-(d[i][1]/d[i][2])^(2*m))/(1+(d[i][2]/d[i][1])^(2*m)))^2
    d[i].append(r)

x = [d[i][0] for i in range(n)]
y = [d[i][3] for i in range(n)]
plt.xlabel('длина волны, нм')
plt.ylabel('R')
plt.title('Зависимость коэффициента отражения от длины волны')
#plt.axis([мин длина волны, макс длина волны, минР, максР])
plt.grid(True)
plt.show()

