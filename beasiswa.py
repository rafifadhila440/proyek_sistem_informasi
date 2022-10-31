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
        print(nama, "berhak mendapatkan beasiswa Bidikmisi")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur IPK")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK \t\t\t: ", ipk)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Bidikmisi")
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
            print(nama, "berhak mendapatkan beasiswa SKTM")
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
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa SKTM")

#Beasiswa Jalur Tahfidz
def beasiswa4():
    #print("=" * 90)
    print("Beasiswa jalur Tahfidz")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    hafalan_juz = int(input("Masukkan jumlah hafalan Juz : "))
    print('')
    os.system('cls')
    if (hafalan_juz >= 10):
        print("=" * 90)
        print("Beasiswa jalur Tahfidz")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah hafalan Juz \t: ", hafalan_juz)
        print(nama, "berhak mendapatkan beasiswa Tahfidz")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Tahfidz")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah hafalan Juz \t: ", hafalan_juz)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Tahfidz")
        print("=" * 90)

#Beasiswa Jalur Influencer Youtube
def beasiswa5():
    print("=" * 90)
    print("Beasiswa Jalur Influencer Youtube")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    jumlah_subscriber = int(input("Masukkan jumlah subscriber : "))
    os.system('cls')
    if (jumlah_subscriber < 3000):
        print("=" * 90)
        print("Beasiswa jalur Influencer Youtube")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah subscriber \t: ", jumlah_subscriber)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Influencer Youtube")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Influencer Youtube")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah subscriber \t: ", jumlah_subscriber)
        print(nama, "berhak mendapatkan beasiswa Influencer Youtube")
        print("=" * 90)

#Beasiswa Jalur Influencer Media Sosial
def beasiswa6():
    print("=" * 90)
    print("Beasiswa Jalur Influencer Media Sosial (TikTok, Instagram dll)")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    jumlah_follower = int(input("Masukkan jumlah pengikut/follower : "))
    os.system('cls')
    if (jumlah_follower < 8000):
        print("=" * 90)
        print("Beasiswa jalur Influencer Media Sosial")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah follower \t: ", jumlah_follower)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Influencer Media Sosial")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Influencer Media Sosial")
        print("Nama penerima beasiswa \t: ", nama)
        print("Jumlah follower \t: ", jumlah_follower)
        print(nama, "berhak mendapatkan beasiswa Influencer Media Sosial")
        print("=" * 90)

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
    print('4. Beasiswa jalur Tahfidz')
    print('5. Beasiswa jalur Influencer Youtube')
    print('6. Beasiswa jalur Influencer Media Sosial')
    print('7. Keluar')

    pilihan = int(input('Jenis beasiswa yang dipilih '))
    os.system('cls')
    if pilihan == 1:
        beasiswa1()
    elif pilihan == 2:
        beasiswa2()
    elif pilihan == 3:
        beasiswa3()
    elif pilihan == 4:
        beasiswa4()
    elif pilihan == 5:
        beasiswa5()
    elif pilihan == 6:
        beasiswa6()
    elif pilihan == 7:
        print("ROGER")
        print("Program diakhiri...")
        print("Sampai Jumpa Lagi :) ")
        kondisi = False
    else:
        print("Maaf input salah")
        print("Opsi tidak tersedia")