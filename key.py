#Память автомобиля:
imb1=70
imb2=90
avto1=27
avto2=38
alf=" 0123456789абвгдеёжзийклмнопрстуфхчцшщъыьэюя"
print(len(alf))

p=20998787 #простое число
#p=1003787
#p=20998787
#p=8 009 097 433
g=5 # первообразный корень

#Функция power
def power(a,x,p):
    if x == 0:
        return 1
    if x % 2 == 0:
        return (power(a, x//2,p)**2)%p
    else:
        return a*power(a, x-1,p)%p

#Генератор ключей Автомобиля
import random
x=random.randint(10000,p-1)
a=power(g,x,p)
print("Открытый ключ A: ",x,a,g,p)

#Генератор ключей Иммобилайзера
y=random.randint(10000,p-1)
b=power(g,y,p)
print("Открытый ключ И: ",y,b,g,p)

#Чтение текста
mes=str(imb1)+input("Введите сообщение: ").lower()+str(avto1)
m=[]
for i in mes:
  if i in alf:
    m.append(alf.index(i))
print(m)

#Процесс шифрования
m1key = power(a, y, p)
print(m1key)
crypto = []
for i in range(len(m)):
    crypto.append(m[i] * m1key % p)

print("Зашифрованное сообщение:", crypto)

#Дешифрование Автомобилем
import time
#Генератор обратного ключа
m2key=power(b,x,p)
print(m2key)
t3=time.time()
mkey_1=power(b,p-1-x,p)
t4=time.time()
print(m2key,mkey_1,m2key*mkey_1 % p)
print(t4-t3)

decrypto=[]

for i in range(len(crypto)):
  decrypto.append(crypto[i]*mkey_1%p)
print("Восстановленное сообщение:", decrypto)

text=""
for i in decrypto:
  text+=alf[i]
print("imb1 -", text[:2])
print("message -", text[2:4])
print("avto1 -", text[4:])

#ВЗЛОМ
#Подслушано шпионом
pz=p
gz=g
ax=a
by=b
from math import *
x=log(a,g)
print(x)
xz = 0
yz = 0
p_new = 0
p_old = 1
for z in range(1, p):
    # Для вывода процентов
    p_new = (100 * z // p)
    if p_new != p_old:
        print(p_new, "%")
        p_old = p_new
    t = power(g, z, p)
    if (t == ax):
        xz = z
        print("x=", z)
    elif (t == by):
        yz = z
        print("y=", z)
    if xz > 0 and yz > 0:
        print("Готово!")
        break
