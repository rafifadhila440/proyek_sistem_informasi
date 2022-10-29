#Proyek Dasar Pemrograman Aplikasi Beasiswa
#Kelompok 3

#Beasiswa Jalur Bidikmisi
import os
def beasiswa1():
    #print("=" * 90)
    print("Beasiswa jalur Bidikmisi")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    print('')
    print("Masukkan penghasilan orang tua/wali")
    print("Contoh: RP 100.000, maka masukkan \"1000000\"")
    penghasilan_ortu = int(input("Masukkan penghasilan : "))
    print('')
    print("Masukkan jumlah anggota keluarga")
    print("Contoh: Banyaknya anggota keluarga adalah tiga orang maka masukkan \"3\"")
    jumlah_anggota_keluarga = int(input("Jumlah anggota keluarga : "))
    os.system('cls')
    if (penghasilan_ortu/jumlah_anggota_keluarga) < 500000:
        print("=" * 90)
        print("Beasiswa jalur Keterangan Kurang Mampu")
        print("Nama penerima beasiswa \t\t: ", nama)
        print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
        print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
        print(nama, "berhak mendapatkan beasiswa")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Keterangan Kurang Mampu")
        print("Nama penerima beasiswa \t\t: ", nama)
        print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
        print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa")
        print("=" * 90)

#Beasiswa Jalur Prestasi
def beasiswa2():
    #print("=" * 90)
    print("Beasiswa jalur Prestasi")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    print('')
    print("Masukkan nilai IPK")
    print("Contoh: IPK 3.00 masukkan \"3.00\"")
    ipk = float(input("IPK : "))
    os.system('cls')
    if (ipk > 4.00 or ipk < 0.00):
        print("Maaf input salah")
    elif (ipk >= 3.50):
        print("=" * 90)
        print("Beasiswa jalur IPK")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK \t\t\t: ", ipk)
        print(nama, "berhak mendapatkan beasiswa")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur IPK")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK \t\t\t: ", ipk)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa")
        print("=" * 90)

#Beasiswa Jalur SKTM
def beasiswa3():
    #print("=" * 90)
    print("Beasiswa jalur SKTM")
    print('')
    nama = input("Masukkan nama calon penerima : ")
    print('')
    print("Masukkan nilai IPK")
    print("Contoh: IPK 3.00 masukkan \"3.00\"")
    ipk = float(input("Nilai IPK : "))
    sktm = input("Apakah anda memiliki SKTM? [ada (y) / tidak (n)] : ")
    os.system('cls')
    if (ipk >= 3.50):
        if (sktm == "ada" or sktm == "y"):
            print("=" * 90)
            print("Beasiswa jalur SKTM")
            print("Nama penerima beasiswa \t: ", nama)
            print("IPK \t\t\t: ", ipk)
            print("SKTM \t\t\t: ", "Ada")
            print("Selamat", nama, "berhak mendapatkan beasiswa")
            print("=" * 90)
        else:
            print("=" * 90)
            print("Beasiswa jalur SKTM")
            print("Nama penerima beasiswa \t: ", nama)
            print("IPK \t\t\t: ", ipk)
            print("SKTM \t\t\t: ", "Belum Ada")
            print("Mohon maaf", nama, "tidak mendapatkan beasiswa,", nama, "harus memiliki SKTM")
            print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur SKTM")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK \t\t\t: ", ipk)
        print("SKTM \t\t\t: ", "Belum Ada")
        print("=" * 90)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa")

#Beasiswa Jalur Prentasi
def beasiswa4():
    print("==========================")
    print("Beasiswa Jalur Prestasi")

#Beasiswa Jalur Talenta
def beasiswa5():
    print("==========================")
    print("Beasiswa Jalur Talenta")

#Beasiswa BIKOM
def beasiswa6():
    print("==========================")
    print("Beasiswa BIKOM")


kondisi = True

#Menu pilihan program
while(kondisi == True):
    print('')
    print("Program Penentuan Beasiswa")
    print("=" * 90)
    print('Pilih kategori beasiswa')
    print('1. Beasiswa jalur Bidikmisi')
    print('2. Beasiswa jalur Prestasi')
    print('3. Beasiswa jalur SKTM')
    print('4. Keluar')

    pilihan = int(input('Jenis beasiswa yang dipilih '))
    os.system('cls')
    if pilihan == 1:
        beasiswa1()
    elif pilihan == 2:
        beasiswa2()
    elif pilihan == 3:
        beasiswa3()
    elif pilihan == 4:
        print("ROGER")
        print("Program diakhiri...")
        print("Sampai Jumpa Lagi :) ")
        kondisi = False
    else:
        print("Maaf input salah")