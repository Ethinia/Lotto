import random
import time

def main():
    lottonumerot = list(range(1,41)) 
    plusnumerot = list(range(1,31))
    oikeatnumerot = []
    lisanumerot = []
    arvottu_plusnumero = []
    pelaajanumerot = []
    pelaaja_plusnumero = []
    oikeinmenneetnumerot = []
    oikeinplusnumerot = []
    oikeinlisanumerot = []

    def pelaajanumerotF():
        plusnumerovalinta = int(input("Anna ensin plusnumero väliltä 1-30: "))
        pelaaja_plusnumero.append(plusnumerovalinta)
        while len(pelaajanumerot) < 7:
            try:
                pelinumerot = int(input("Anna lotto numero väliltä 1-40: "))
                if pelinumerot not in range(0,41):
                    print("Voit antaa numeroita vain väliltä 1-40")
                elif pelinumerot not in pelaajanumerot:
                    pelaajanumerot.append(pelinumerot)
                elif pelinumerot in pelaajanumerot:
                    print("Et voi valita samaa numeroa kahdesti")
            except ValueError:
                print("Syötä numeroita")
                continue
    
    def oikeatnumerotF():
        kierrokset1 = 0
        for arvottunumero in lottonumerot:
            if kierrokset1 == 7:
                break
            arvottunumero = random.choice(lottonumerot)
            oikeatnumerot.append(arvottunumero)
            lottonumerot.remove(arvottunumero)          
            kierrokset1 += 1

    def lisanumerotF():
            lisanumero = random.choice(lottonumerot)
            lisanumerot.append(lisanumero)
            lottonumerot.remove(lisanumero)          

    def plusnumerotF():
            plusnumero = random.choice(plusnumerot)
            arvottu_plusnumero.append(plusnumero)
            plusnumerot.remove(plusnumero)          

    def montakooikein(oikeatnumerot):
        for pelaaja in oikeatnumerot:
            if pelaajanumerot.count(pelaaja):
                oikeinmenneetnumerot.append(pelaaja)
        for pelaaja in lisanumerot:
             if pelaajanumerot.count(pelaaja):
                oikeinlisanumerot.append(pelaaja)
        for pelaaja in arvottu_plusnumero:
             if pelaaja_plusnumero.count(pelaaja):
                 oikeinplusnumerot.append(pelaaja)

    def voittovalinta():
        if len(oikeinplusnumerot) != 0 and len(oikeinmenneetnumerot) != 7:
            plusvoitto()
        else:
            normaalivoitto()
    
    def plusvoitto():
        print(3*"\n")
        if  len(oikeinmenneetnumerot) == 6 and len(oikeinlisanumerot) == 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} arvottua numeroa, lisänumeron ja plus numeron oikein. Voitit 1 000 000€")
        if  len(oikeinmenneetnumerot) == 6 and len(oikeinlisanumerot) != 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} arvottua numeroa ja plus numeron oikein. Voitit 103 788€")
        if len(oikeinmenneetnumerot) == 5:
            print (f"\nSait {len(oikeinmenneetnumerot)} arvottua numeroa ja plus numeron oikein. Voitit 3276€")
        if len(oikeinmenneetnumerot) == 4:
            print (f"\nSait {len(oikeinmenneetnumerot)} arvottua numeroa ja plus numeron oikein. ja voitit 90€")
        if len(oikeinmenneetnumerot) == 3 and len(oikeinlisanumerot) == 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} arvottua numeroa, lisänumeron ja plus numeron oikein. voitit 10€")    
        if len(oikeinmenneetnumerot) == 1:
            print (f"\nei voittoa tällä kertaa. Sait yhden({len(oikeinmenneetnumerot)}) numeron oikein. Parempaa onnea seuraavalle kerralle!")
        if  len(oikeinmenneetnumerot) == 2 or len(oikeinmenneetnumerot) ==3:
            print (f"\nei voittoa tällä kertaa. Sait {len(oikeinmenneetnumerot)} numeroa oikein. Parempaa onnea seuraavalle kerralle!")
        if len(oikeinmenneetnumerot) == 0:
            print (f"\n(Sait pelkän plus numeron oikein. Voitit 5€")
        print(2*"\n")
        print(f"Sinun numerosi olivat {list(sorted(pelaajanumerot))}")
        print(f"Oikeat numerot olivat {list(sorted(oikeatnumerot))}")
        print(f"Lisänumero oli {lisanumerot} ja plus numero oli {arvottu_plusnumero}")

    def normaalivoitto():
        print(3*"\n")
        if len(oikeinmenneetnumerot) == 7:
            print ("\nPÄÄVOITTO!!! Voitit 2.5 miljoonaa euroa!")
        if  len(oikeinmenneetnumerot) == 6 and len(oikeinlisanumerot) == 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} oikeaa numeroa, yhden oikean lisänumeron ja voitit 513 457€")
        if  len(oikeinmenneetnumerot) == 6 and len(oikeinlisanumerot) != 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} oikeaa numeroa ja voitit 11 532€")
        if len(oikeinmenneetnumerot) == 5:
            print (f"\nSait {len(oikeinmenneetnumerot)} oikeaa numeroa ja voitit 364€")
        if len(oikeinmenneetnumerot) == 4:
            print (f"\nSait {len(oikeinmenneetnumerot)} oikeaa numeroa ja voitit 10€")
        if len(oikeinmenneetnumerot) == 3 and len(oikeinlisanumerot) == 1:
            print (f"\nSait {len(oikeinmenneetnumerot)} oikeaa numeroa, yhden oikean lisänumeron ja voitit 2€")
        if len(oikeinmenneetnumerot) == 1:
            print (f"\nei voittoa tällä kertaa. Sait yhden({len(oikeinmenneetnumerot)}) numeron oikein. Parempaa onnea seuraavalle kerralle!")
        if  len(oikeinmenneetnumerot) == 0 or len(oikeinmenneetnumerot) == 2 or len(oikeinmenneetnumerot) == 3:
            print (f"\nei voittoa tällä kertaa. Sait {len(oikeinmenneetnumerot)} numeroa oikein. Parempaa onnea seuraavalle kerralle!")
        print(2*"\n")
        print(f"Sinun numerosi olivat {list(sorted(pelaajanumerot))}")
        print(f"Oikeat numerot olivat {list(sorted(oikeatnumerot))}")
        print(f"Lisänumero oli {lisanumerot} ja plus numero oli {arvottu_plusnumero}")

    pelaajanumerotF()
    oikeatnumerotF()
    lisanumerotF()
    plusnumerotF()
    montakooikein(oikeatnumerot)
    print(15*"\n")
    print("\nArvotaan 7 numeroa")
    print(10*"\n")
    time.sleep(2)
    voittovalinta()

kierroksetL = 0
while True:
    if kierroksetL == 0:
        print(2*"\n")
        print(" _        _______ __________________ _______ ")
        print("( \      (  ___  )\__   __/\__   __/(  ___  )")
        print("| (      | (   ) |   ) (      ) (   | (   ) |")
        print("| |      | |   | |   | |      | |   | |   | |")
        print("| |      | |   | |   | |      | |   | |   | |")
        print("| |      | |   | |   | |      | |   | |   | |")
        print("| (____/\| (___) |   | |      | |   | (___) |")
        print("(_______/(_______)   )_(      )_(   (_______)")
        print(2*"\n")
        pelireset = input("\nTervetuloa! Haluatko pelata lottoa? (k/e):  ")
        if pelireset == "k":
            main()
        elif pelireset == "e":
            break
        kierroksetL +=1
    else: 
        pelireset = input("\nHaluatko pelata uudestaan? (k/e):  ")
        if pelireset == "k":
            main()
        elif pelireset == "e":
            break
