#bekérés jön itten bizony
be=input("Kérek egy számot: ")
print(be)

if be % 2 == 0:
    print("páros")
else:
    print("páratlan")


ora=int(input("Hány óra van?"))
if ora<= 8:
    print("Jó reggelt!")
elif ora<= 17:
    print("Jó napot!")
elif ora<= 21:
    print("Jó estét!")
else:
    print("Jó éjszakát")
