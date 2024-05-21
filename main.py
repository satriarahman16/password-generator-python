import random

lst_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst_numbers = [0,1,2,3,4,5,6,7,8,9]
lst_symbols = [
    # Tanda baca umum
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Ini ada tools untuk membuatkan password yang sulit !")

jumlah_alphabet = int(input("masukkan jumlah karakter berupa alphabet yang diinginkan dengan angka\n"))
jumlah_angka = int(input("masukkan jumlah karakter berupa angka yang diinginkan dengan angka\n"))
jumlah_symbols = int(input("masukkan jumlah karakter berupa symbols yang diinginkan dengan angka\n"))

password = []
password_oke = ''

for i in range(1, jumlah_alphabet+1):
    password.append(random.choice(lst_alphabets))

for i in range(1, jumlah_angka+1):
    password.append(random.choice(lst_numbers))

for i in range(1, jumlah_symbols+1):
    password.append(random.choice(lst_symbols))

random.shuffle(password)

for i in password:
    password_oke += str(i)

print(password_oke)