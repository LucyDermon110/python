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
bacil_price = 5000
money = 100000
input_count = input('Mau berapa bungkus? ')
count = int(input_count)
total_price = bacil_price * count
print('Anda akan membeli ' + str(count) + ' bacil')
print('Harga total adalah ' + str(total_price) + ' rupiah')
if money > total_price:
    print('Anda telah membeli ' + str(count) + ' bacil')
    print('Uang Anda tinggal ' + str(money - total_price) + ' rupiah')
elif money == total_price:
    print('Anda telah membeli ' + str(count) + ' bacil')
    print('Dompet Anda kosong')
else:
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli bacil sebanyak itu')