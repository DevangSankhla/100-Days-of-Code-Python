from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z' ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number(1-25):\n"))

def encrypt(ogtext, shiftamt):
    textlist = []
    encryptedtext = []
    for letter in ogtext:
        if letter in alphabet:
            newindex = alphabet.index(letter) + shiftamt
            textlist.append(newindex)
            encryptedtext.append(alphabet[newindex])
        else:
            encryptedtext.append(letter)
    et = '' .join(encryptedtext)
    print(f'here is you encrypted text, remember the shift no.\n {et}')

def decrypt(ogtext,shiftamt):
    textlist2 = []
    decryptedtext = []
    for letter in ogtext:
        if letter in alphabet:
            newindex2 = alphabet.index(letter) - shiftamt
            textlist2.append(newindex2)
            decryptedtext.append(alphabet[newindex2])
        else:
            decryptedtext.append(letter)
    dt = '' .join(decryptedtext)
    print(f'here is you decrypted text \n{dt}')


if direction == 'encode' or direction =='encrypt':
    encrypt(ogtext = text,shiftamt= shift)
else:
    decrypt(ogtext = text,shiftamt =shift)
