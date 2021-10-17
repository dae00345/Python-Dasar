from os import system

def cls():
    return system('cls')

#==============================
def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
        except ValueError:
            cls()
            print('\n| WARNING | : Inputan Hanya Menerima Angka')
        else:
            return ipt
#==============================

#==============================
def jwb(pesan):
    ipt = input(pesan).lower()
    while ipt != "y" and ipt != "t":
        print("\n |> Masukkan Y atau T saja")
        ipt = input(pesan).lower()
    return ipt
#==============================

#==============================
def tambah(num1,num2):
    return num1+num2

def kurang(num1,num2):
    return num1 - num2

def kali(num1,num2):
    return num1*num2

def bagi(num1,num2):
    return num1/num2
#==============================

#main
def main():
    ulang = 'y'
    while ulang == 'y':
        cls()
        num1 = angka("| >> Num1 : ")
        num2 = angka("| >> Num2 : ")
        pil = angka("| >> Operasi : ")
        while pil < 1 or pil > 4:
            print("\n Pilihan Operasi Tidak Tersedia")
            pil = angka("| >> Operasi : ")

        #pengkondisian
        if pil ==1:
            hasil = tambah(num1,num2)
        elif pil ==2:
            hasil = kurang(num1,num2)
        elif pil ==3:
            hasil = kali(num1,num2)
        elif pil ==4:
            hasil = bagi(num1,num2)
        else:
            pass

        print("\nHasil : ",hasil)
        ulang = jwb("| >> Ulangi Program <y/t> : ")

main()
