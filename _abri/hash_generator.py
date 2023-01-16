import secrets

# generate a random hash
hash_val = secrets.token_hex()

# write the hash to a file
with open("hash.txt", "w") as hash_file:
    hash_file.write(hash_val)

print(hash_val)
input()