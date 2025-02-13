
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(original_text, shift_n):
    ref_alphabet = shifter(shift_n)

    message_encrypt = ""
    for i in original_text:
        if i in alphabet:
            index = alphabet.index(i)
            message_encrypt += ref_alphabet[index]
        else:
            message_encrypt += i

    return message_encrypt

def decrypt(encrypted_text, shift_n):
    ref_alphabet = shifter(shift_n)

    message_decrypt = ""
    for i in encrypted_text:
        if i in ref_alphabet:
            index = ref_alphabet.index(i)
            message_decrypt += alphabet[index]
        else:
            message_decrypt += i

    return message_decrypt

def shifter(shift_n):
    ref_alphabet = alphabet.copy()
    alt_alphabet = []

    for i in range(0, shift_n + 1):
        alt_alphabet.extend(alphabet[i])
        ref_alphabet.remove(alphabet[i])
    return ref_alphabet + alt_alphabet

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift: "))

    if direction == "encode":
        print(f": {encrypt(text, shift)}")
    elif direction == "decode":
        print(f": {decrypt(text, shift)}")
    else:
        break
