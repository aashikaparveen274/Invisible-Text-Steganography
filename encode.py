# Invisible symbols
ZWSP = '\u200b'
ZWNJ = '\u200c'

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

normal_text = input("Enter normal text: ")
secret = input("Enter secret message: ")

binary = text_to_binary(secret)

hidden = binary.replace('0', ZWSP).replace('1', ZWNJ)

final_text = normal_text + hidden

with open("secret.txt", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Secret hidden successfully!")
