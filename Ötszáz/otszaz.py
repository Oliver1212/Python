f=open("penztar.txt")
kosar=[]

for sor in f:
    kosar.append(sor.strip())

f.close()

print("2. feladat")
print("a fizetések száma: " + str(kosar.count("F")))

print("3.feladat")
print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")

sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucik neve: ")
darab=int(input("Darabszám:"))

aruindex=kosar.index(arunev)
darablista=kosar[:aruindex]
print(darablista)
vasarlasDb=darablista.count("F") +1
print(vasarlasDb)

print("5. feladat")
print("Az első vásárlás sorszáma: " + str(vasarlasDb))

utolsoindex=0
for i in range(0,len(kosar)):
    if kosar[i*-1-1]==arunev:
        utolsoindex=len(kosar)-i
        break
darablista=kosar[utolsoindex]
vasarlasDb=darablista.count("F") + 1
print("Az utolsó vásárlás sorszáma: " + str(vasarlasDb))

voltF=False
szam=0
for e in kosar:
    if e==arunev:
        























        
    
