class ember:
    def __init__(self,nev):
        self.nev=nev
    def beszel(self):
        print("valami(" + self.nev+")")

e=ember("István")
e.beszel()
print(e.nev)
e.nev="József"
print(e.nev)

class ferfi(ember):
    def magas(self):
        print(self.nev + ": valami")
    def beszel(self):
        print("valami")

f=ferfi("Ferenc")
f.beszel()
f.magas()

f2=ferfi("Zsigmond")
f2.magas()
