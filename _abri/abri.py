import hashlib

# read the hashed password from the hash.txt file
with open("hash.txt", "r") as hash_file:
    hash = hash_file.read().strip()

key = input("Введите ключ: ")

if key == hash:
    exec(open("main.py").read())
else:
    print("Неправильный ключ")
    input()