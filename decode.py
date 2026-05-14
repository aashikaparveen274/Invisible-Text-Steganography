ZWSP = '\u200b'
ZWNJ = '\u200c'

def binary_to_text(binary):

    letters = [
        binary[i:i+8]
        for i in range(0, len(binary), 8)
    ]

    return ''.join(chr(int(b, 2)) for b in letters)

with open("secret.txt", "r", encoding="utf-8") as f:
    text = f.read()

hidden = ''.join(c for c in text if c in [ZWSP, ZWNJ])

binary = hidden.replace(ZWSP, '0').replace(ZWNJ, '1')

message = binary_to_text(binary)

print("Secret Message:")
print(message)