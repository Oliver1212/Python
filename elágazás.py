#bekérés jön itten bizony
be=input("Kérek egy számot: ")
print(be)

if be % 2 == 0:
    print("páros")
else:
    print("páratlan")
    
szam=int(input("Kérek mé egy számot"))
if szam > 10:
    if szam % 12 == 0:
        print ((str)szam) + "osztható 12-vel")
    else:
        print((str)szam) +"nem oszthato 12-vel")
