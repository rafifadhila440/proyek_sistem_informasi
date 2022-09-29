#Program beasiswa ceritanya
#Dasar Pemrograman
#Developer Kelompok 3

def beasiswa1():
    print('')
    print("Masukkan penghasilan orang tua/wali")
    print("Format: misal penghasilan RP 100.000, inputkan \"1000000\"")
    portu = int(input("Input: "))
    print('')
    print("Masukkan banyaknya anggota keluarga")
    print("Format: misal banyaknya anggota keluarga adalah tiga orang maka inputkan \"3\"")
    janggotak = int(input("Input: "))
    if (portu/janggotak) < 500000:
        print('')
        print("Berhak mendapatkan beasiswa")
    else:
        print('')
        print("Tidak berhak mendapatkan beasiswa")

def beasiswa2():
    print("Masukkan IPK")
    print("Format: misal IPK 3.00 masukkan 3.00")
    ipk = float(input("IPK: "))
    if (ipk > 4.00 or ipk < 0.00):
        print("Input salah")
    elif (ipk >= 3.00):
        print('')
        print("Berhak mendapatkan beasiswa")
    else:
        print('')
        print("Tidak berhak mendapatkan beasiswa")

kondisi = True

while(kondisi == True):
    print('')
    print("Program Penentuan Beasiswa")
    print("================================")
    print('Pilih jenis beasiswa')
    print('1. Beasiswa kurang mampu')
    print('2. Beasiswa prestasi akademik')
    print('3. Keluar')

    pilihan = int(input('Jenis beasiswa yang dipilih '))
    if pilihan == 1:
        beasiswa1()
    elif pilihan == 2:
        beasiswa2()
    elif pilihan == 3:
        print("Program diakhiri...")
        kondisi = False
    else:
        print("Input salah")