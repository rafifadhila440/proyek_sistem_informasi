#Program beasiswa ceritanya
#Dasar Pemrograman
#Developer Kelompok 3

def beasiswa1():
    print("Beasiswa jalur keterangan kurang mampu")
    print('')
    print("Masukkan penghasilan orang tua/wali")
    print("Contoh: RP 1.000.000, inputkan \"1000000\"")
    penghasilan_ortu = int(input("Input: "))
    print('')
    print("Masukkan banyaknya anggota keluarga")
    print("Format: misal banyaknya anggota keluarga adalah tiga orang maka inputkan \"3\"")
    jumlah_anggota_keluarga = int(input("Input: "))
    if (penghasilan_ortu/jumlah_anggota_keluarga) < 500000:
        print('')
        print("Selamat anda mendapatkan beasiswa")
    else:
        print('')
        print("Mohon maaf anda tidak mendapatkan beasiswa")

def beasiswa2():
    print("Beasiswa jalur IPK")
    print("Masukkan IPK")
    print("Contoh: IPK 3.00 masukkan 3.00")
    ipk = float(input("IPK: "))
    if (ipk > 4.00 or ipk < 0.00):
        print("Input salah")
    elif (ipk >= 3.00):
        print('')
        print("Selamat anda mendapatkan beasiswa")
    else:
        print('')
        print("Mohon maaf anda tidak mendapatkan beasiswa")

def beasiswa3():
    print("Beasiswa jalur KIP")
    print(" ")

def beasiswa4():
    print("Beasiswa Jalur Prestasi")
    print(" ")

def beasiswa5():
    print("Beasiswa Jalur Talenta")
    print(" ")

def beasiswa6():
    print("Beasiswa BIKOM")
    print(" ")


kondisi = True

while(kondisi == True):
    print('')
    print("Program Penentuan Beasiswa")
    print("================================")
    print('Pilih kategori beasiswa')
    print('1. Beasiswa kurang mampu')
    print('2. Beasiswa jalur IPK')
    print('3. Beasiswa jalur KIP')
    print('4. Beasiswa jalur Prestasi')
    print('5. Beasiswa jalur Talenta')
    print('6. Beasiswa jalur Bikom')
    print('7. Keluar')

    pilihan = int(input('Jenis beasiswa yang dipilih '))
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
        beasiswa6    
    elif pilihan == 7:
        print("Program diakhiri...")
        kondisi = False
    else:
        print("Input salah")