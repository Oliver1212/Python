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
