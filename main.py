from random import sample as sp
from random import randint as rt
import matplotlib.pyplot as plt

mov={1:-3, 2:1, 3:3, 4:-1}
tab=[1,2,3,4,5,6,7,8,9]
dic = {1:[2,3], 2:[2,3,4], 3:[3,4], 4:[1,2,3], 5:[1,2,3,4], 6:[1,3,4], 7:[1,2], 8:[1,2,4], 9:[1,4]}

n=100000    #tentativas

histo=[]
t=0
p = sp(tab, 1)[0]

def Move():
    global p
    a = sp(dic[p],1)
    p += mov[a[0]]

for i in range(n):
    v=0
    while v==0:
        r = 0
        while r<3:
            x = rt(1,9)
            t+=1
            r+=1
            if x==p:
                histo.append(t)     # local
                # with open('out.txt','a') as arq:   # Para exportar os dados em linhas
                #     arq.writelines([str(t),'\n'])
                p = sp(tab, 1)[0]
                t = 0
                v=1
                break
            elif r==3:
                Move()


w=0.99     # Quantil

histo.sort()

q = int(round(((w*n)),0))
print(f'{w*100}% de chance de acertar com até {histo[q-1]} jogadas.')

plt.hist(histo, 50, rwidth=1)
plt.show()
