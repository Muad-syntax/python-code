import random

angka_rahasia = random.randint(1, 100)
ronde = 0 
max_ronde = 7

print("===== TEBAK ANGKA =====")
print("Ada angka 1 sampai 100, coba tebak angka apa?")
print("Anda punya " + str(max_ronde) + " kesempatan untuk menebak")

while(ronde < max_ronde):
    tebakan = int(input("Tebakan Kamu: "))
    ronde += 1

    if (tebakan < angka_rahasia):
        print("Tebakan terlalu kecil!")
    elif (tebakan > angka_rahasia):
        print("Tebakan terlalu besar!")
    else :
        print("SELAMAT!, jawaban anda benar")
        exit(0)
    print("Sisa kesempatan " + str(max_ronde - ronde))
    print("_______________________________")

print("Kesempatan habis.... ")
print("Angkanya adalah " + str(angka_rahasia))