import getpass
user = input("masukkan username: ")
kata_sandi = getpass.getpass()
if kata_sandi == '030604' and user == 'Lucydermon':
    print("\033[1;33;40m====================----------- Anda telah login ----------===================")
    print("\033[1;33;40m====================---- Selamat datang di Program saya ----==================")
    print("\033[1;33;40mHalo "+user)
else:
    print("\033[1;33;40m Password atau username salah")
    print("\033[1;33;40m Harap Coba Lagi")
print("Kami menjual buah-buahan")
print("Anda mau buah apa?")
print("silahkan pilih buah-buahan di bawah ini")
fruits = ['Apel','Jeruk','Semangka','Rambutan','Mangga','Pisang']
result = ''
for fruit in fruits:
    result += fruit + ' '
print(result)
pilihan = input("Pilih jenis buah : ")
if pilihan == 'Apel':
    print ("Anda memilih buah Apel")
elif pilihan == 'Jeruk':
    print("Anda memilih buah Jeruk")
elif pilihan == 'Semangka':
    print ("Anda memilih buah Semangka")
elif pilihan == 'Rambutan':
    print ("Anda memilih buah Rambutan")
elif pilihan == 'Mangga':
    print ("Anda memilih buah Mangga")
elif pilihan == 'Pisang':
    print ("Anda memilih buah Pisang")
else:
    print("Maaf buah yang anda pilih belum tersedia")