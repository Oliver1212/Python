#bek�r�s j�n itten bizony
be=input("K�rek egy sz�mot: ")
print(be)

if be % 2 == 0:
    print("p�ros")
else:
    print("p�ratlan")


ora=int(input("H�ny �ra van?"))
if ora<= 8:
    print("J� reggelt!")
elif ora<= 17:
    print("J� napot!")
elif ora<= 21:
    print("J� est�t!")
else:
    print("J� �jszak�t")
