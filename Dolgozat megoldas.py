import random

f=open("adatok.txt","w")

be=int(input("Kérek egy számot: "))
for i in range(0,be):
    szam=random.randint(0,12)
    f.write(str(szam)+"\n")

f.close()


f=open("adatok.txt",)
#s=f.read()
#print(s)
lista=[]
for sor in f:
    lista.append(int(sor))
    print(lista)

f.close()

osszeg=0
for szam in lista:
    osszeg+=szam
print(osszeg)
f=open("adatok.txt","a")
f.write(str(osszeg))

f.close()
