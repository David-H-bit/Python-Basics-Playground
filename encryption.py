import random, string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter some text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print()
print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")
print()

plain_text = ""
cipher_text = input("Enter some text to decrypt: ")

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print()
print(f"encrypted message: {cipher_text}")
print(f"decrypted message: {plain_text}")
print()
