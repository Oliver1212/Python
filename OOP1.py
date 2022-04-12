#osztály definíció

class kutya:
    #konstruktor
    def __init__(self,nev):
        self.nev=nev
    #osztály függvény
    def ugat(self):
        print("vau-vau(" + self.nev+")")
#példányosítás
k=kutya("Armageddon")
k.ugat()
print(k.nev)
#osztályváltozó értékadása
k.nev="Bruno"
print(k.nev)
#Öröklés,leszármasztatás
class NemetJuhasz(kutya):
    #új függvény
    def pitiz(self):
        print(self.nev + ": Nein!!!")
    #függvény felűlírás
    def ugat(self):
        print("wau-wau")
        
n=NemetJuhasz("Rex")
n.ugat()
n.pitiz()

n2=NemetJuhasz("Kondér")
n2.pitiz()
