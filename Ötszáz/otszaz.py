def ertek(darab):
    if darab==1:
        return 500
    else:
        return darab*400+150


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
        if not voltF:
            szam=szam + 1
            voltF=True
    if e=="F":
        voltF=False

print(str(szam) + "vásárlás során vettek belőle.")

print("6. feladat")
print(str(vasarlasDb)+ "darab vételekor fizetendő: " + str(ertek(vasarlasDb)))

darabF=0
elozoindex=0
keresettindex=0

for i in range(0,len(kosar)):
    if kosar[i]=="F":
        darabF+=1
    if darabF==sorszam:
        elozoindex=keresettindex
        keresettindex=i
        break

print(kosar[elozoindex-1:keresettindex])
if sorszam>1:
    darabkosar=kosar[elozoindex+1:keresettindex]
else:
    darabkosar=kosar[elozoindex:keresettindex]
stat={}
for e in darabkosar:
    if e in stat.keys():
        stat[e]+=1
    else:
        stat[e]=1

print(stat)
























        
    
