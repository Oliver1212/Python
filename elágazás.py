#bek�r�s j�n itten bizony
be=input("K�rek egy sz�mot: ")
print(be)

if be % 2 == 0:
    print("p�ros")
else:
    print("p�ratlan")
    
szam=int(input("K�rek m� egy sz�mot"))
if szam > 10:
    if szam % 12 == 0:
        print ((str)szam) + "oszthat� 12-vel")
    else:
        print((str)szam) +"nem oszthato 12-vel")
