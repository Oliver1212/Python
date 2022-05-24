szam=""

while szam=="":
    try:
        szam=int(input("Kérek egy számot: "))
    except:
        print("Ez nem szám!")
    else:
        print("Most mi van?")
    finally:
        print("Ezzel megvolnánk")
print(szam*2)
