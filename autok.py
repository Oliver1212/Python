f=open("autok.txt","r")
teljes=f.read()
#print(teljes)

f.close()
teljes=teljes[0:-1]
darabok=teljes.split("\n")
#print(darabok)

for egySor in darabok:
    vag=egySor.split(" ")
    print(vag[2])

