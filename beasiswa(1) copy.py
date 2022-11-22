#Proyek Dasar Pemrograman Aplikasi Beasiswa
#Kelompok 3

#Beasiswa Jalur Keterangan Kurang Mampu
import os
def beasiswa1():
    #print("=" * 90) 
    #Input Data Mhs
    print("Beasiswa jalur Keterangan Kurang Mampu")
    print('')
    nim = int(input("Masukkan NIM penerima beasiswa : "))
    nama = input("Masukkan nama penerima beasiswa : ")
    print('')

    #Input Fakultas
    print("Masukkan asal Fakultas Kampus Mantap")
    print("Contoh: Jika asal dari Fakultas Teknik Dan Informatika, masukkan \"Teknik dan Informatika\"")
    fakultas = input("Fakultas : ")
    print('')
    
    #Input Prodi
    print("Masukkan Prodi Fakultas Kampus Mantap")
    print("Contoh: Jika prodi Teknik Informatika, masukkan \"Teknik Informasika\"")
    prodi = input("Prodi : ")
    print('')

    #Input Penghasilan Orang Tua dan Jumlah Anggota Keluarga
    print("Masukkan penghasilan orang tua/wali")
    print("Contoh: RP 100.000, maka masukkan \"1000000\"")
    penghasilan_ortu = int(input("Masukkan penghasilan (Min. 1500000) : "))
    print('')
    print("Masukkan jumlah anggota keluarga")
    print("Contoh: Banyaknya anggota keluarga adalah tiga orang maka masukkan \"3\"")
    jumlah_anggota_keluarga = int(input("Jumlah anggota keluarga : "))
    print("Apakah penerima beasiswa memiliku SKTM (Surat Keterangan Tidak Mampu)? ")
    sktm = input("[ada (y) / tidak (n)] : ")
    
    #Proses
    total = penghasilan_ortu / jumlah_anggota_keluarga
    #os.system('cls')

    #Output
    if (total <= 1500000) :
        if (sktm == "y" or sktm == "Y"):
            sktm = "Ada"
            print("=" * 90)
            print("Beasiswa jalur Keterangan Kurang Mampu\n")
            print("Nim penerima beasiswa \t\t: ", nim)
            print("Nama penerima beasiswa \t\t: ", nama)
            print("Asal Fakultas \t\t\t: ", fakultas)
            print("Prodi Fakultas \t\t\t: ", prodi)
            print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
            print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
            print("SKTM \t\t\t\t: ", sktm)
            print(nama, "berhak mendapatkan beasiswa")
            print("=" * 90)
            opsi = input("Tekan Y untuk kembali ke menu :")
            os.system('cls')
            if (opsi == "y" or opsi == "Y"):
                kondisi == True

        elif (sktm == "n" or sktm == "N"):
            sktm = "Belum Ada"
            print("=" * 90)
            print("Beasiswa jalur Keterangan Kurang Mampu\n")
            print("Nim penerima beasiswa \t\t: ", nim)
            print("Nama penerima beasiswa \t\t: ", nama)
            print("Asal Fakultas \t\t\t: ", fakultas)
            print("Prodi Fakultas \t\t\t: ", prodi)
            print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
            print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
            print("SKTM \t\t\t\t: ", sktm)
            print("Mohon maaf", nama, "tidak mendapatkan beasiswa karena belum ada surat SKTM.")
            print("Silakan coba lagi")
            print("=" * 90)
            opsi = input("Tekan Y untuk kembali ke menu :")
            os.system('cls')
            if (opsi == "y" or opsi == "Y"):
                kondisi == True

    elif (total >= 1500000):
        if (sktm == "y" or sktm == "Y"):
            sktm = "Ada"
            print("=" * 90)
            print("Beasiswa jalur Keterangan Kurang Mampu\n")
            print("Nim penerima beasiswa \t\t: ", nim)
            print("Nama penerima beasiswa \t\t: ", nama)
            print("Asal Fakultas \t\t\t: ", fakultas)
            print("Prodi Fakultas \t\t\t: ", prodi)
            print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
            print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
            print("SKTM \t\t\t\t: ", sktm)
            print("Mohon maaf", nama, "tidak mendapatkan beasiswa karena penghasilan diatas kriteria.")
            print("Silakan coba lagi")
            print("=" * 90)
            opsi = input("Tekan Y untuk kembali ke menu :")
            os.system('cls')
            if (opsi == "y" or opsi == "Y"):
                kondisi == True

        elif (sktm == "n" or sktm == "N"):
            sktm = "Belum Ada"
            print("=" * 90)
            print("Beasiswa jalur Keterangan Kurang Mampu\n")
            print("Nim penerima beasiswa \t\t: ", nim)
            print("Nama penerima beasiswa \t\t: ", nama)
            print("Asal Fakultas \t\t\t: ", fakultas)
            print("Prodi Fakultas \t\t\t: ", prodi)
            print("Penghasilan Orang Tua/Wali \t: ", penghasilan_ortu)
            print("Jumlah anggota keluarga \t: ", jumlah_anggota_keluarga)
            print("SKTM \t\t\t\t: ", sktm)
            print("Mohon maaf", nama, "tidak mendapatkan beasiswa karena penghasilan diatas kriteria dan belum ada surat SKTM.")
            print("Silakan coba lagi")
            print("=" * 90)
            opsi = input("Tekan Y untuk kembali ke menu :")
            os.system('cls')
            if (opsi == "y" or opsi == "Y"):
                kondisi == True

#Beasiswa Jalur Prestasi
def beasiswa2():
    #print("=" * 90)
    print("Beasiswa jalur Prestasi")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    print('')
    print("Masukkan nilai IPK")
    print("Contoh: IPK 3.00 masukkan \"3.00\"")
    ipkd1 = float(input("IPK D1 : "))
    ipkd2 = float(input("IPK D2 : "))
    ipkd3 = float(input("IPK D3 : "))
    ipks1 = float(input("IPK S1 : "))
    ipktotal = ipkd1 + ipkd2 + ipkd3
    ipkrata = ipktotal / 3
    format_ipkrata = "{:.2f}".format(ipkrata)
    #os.system('cls')
    if (ipkrata > 4.00 or ipkrata < 0.00):
        print("IPK terlalu besar")
    elif (ipkrata >= 3.50):
        print("=" * 90)
        print("Beasiswa jalur Prestasi")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK rata-rata \t\t: ", format_ipkrata)
        print(nama, "berhak mendapatkan beasiswa Prestasi")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Prestasi")
        print("Nama penerima beasiswa \t: ", nama)
        print("IPK rata-rata \t\t: ", format_ipkrata)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Prestasi")
        print("=" * 90)

#Beasiswa Jalur Tahfidz
def beasiswa3():
    #print("=" * 90)
    #Input Data Mhs
    print("Beasiswa jalur Tahfidz")
    print('')
    nim = int(input("Masukkan NIM penerima beasiswa : "))
    nama = input("Masukkan nama penerima beasiswa : ")
    print('')

    #Input Fakultas
    print("Masukkan asal Fakultas Kampus Mantap")
    print("Contoh: Jika asal dari Fakultas Teknik Dan Informatika, masukkan \"Teknik dan Informatika\"")
    fakultas = input("Fakultas : ")
    print('')

    #Input Prodi
    print("Masukkan Prodi Fakultas Kampus Mantap")
    print("Contoh: Jika prodi Teknik Informatika, masukkan \"Teknik Informasika\"")
    prodi = input("Prodi : ")
    print('')

    #Input jumlah hafalan
    print("Masukkan jumlah hafalan Juz\nMinimal 10 Juz")
    hafalan_juz = int(input("Jumlah hafalan Juz : "))
    print('')
    #os.system('cls')
    if (hafalan_juz >= 10):
        print("=" * 90)
        print("Beasiswa jalur Tahfidz")
        print("Nim penerima beasiswa \t: ", nim)
        print("Nama penerima beasiswa \t: ", nama)
        print("Asal Fakultas \t\t: ", fakultas)
        print("Prodi Fakultas \t\t: ", prodi)
        print("Jumlah hafalan Juz \t: ", hafalan_juz)
        print(nama, "berhak mendapatkan beasiswa Tahfidz")
        print("=" * 90)
    else:
        print("=" * 90)
        print("Beasiswa jalur Tahfidz")
        print("Nim penerima beasiswa \t: ", nim)
        print("Nama penerima beasiswa \t: ", nama)
        print("Asal Fakultas \t\t: ", fakultas)
        print("Prodi Fakultas \t\t: ", prodi)
        print("Jumlah hafalan Juz \t: ", hafalan_juz)
        print("Mohon maaf", nama, "tidak mendapatkan beasiswa Tahfidz.\nMinimal hafalan 10 Juz.")
        print("=" * 90)

#Beasiswa Jalur Influencer Youtube
def beasiswa4():
    print("=" * 90)
    print("Beasiswa Jalur Influencer Youtube")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    jumlah_subscriber = int(input("Masukkan jumlah subscriber : "))
    #os.system('cls')
    if (jumlah_subscriber < 5000):
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
def beasiswa5():
    print("=" * 90)
    print("Beasiswa Jalur Influencer Media Sosial (TikTok, Instagram dll)")
    print('')
    nama = input("Masukkan nama penerima beasiswa : ")
    jumlah_follower = int(input("Masukkan jumlah pengikut/follower : "))
    #os.system('cls')
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
    print('1. Beasiswa jalur Keterangan Kurang Mampu')
    print('2. Beasiswa jalur Prestasi')
    print('3. Beasiswa jalur Tahfidz')
    print('4. Beasiswa jalur Influencer Youtube')
    print('5. Beasiswa jalur Influencer Media Sosial')
    print('6. Keluar')

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
        print("ROGER")
        print("Program diakhiri...")
        print("Sampai Jumpa Lagi :) ")
        kondisi = False
    else:
        print("Maaf input salah")
        print("Opsi tidak tersedia")