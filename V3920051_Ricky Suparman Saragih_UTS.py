import math 
plaintext = input("masukan plaintext : ")
key, keyA, keyB = input("masukkan key : "), int(input("key A : ")), int(input("key B : "))

def keygenerator(Plaintext, key):
    key = list(key)
    if len(key) == len(Plaintext):
        return key
    else:
        for x in range(len(Plaintext)-len(key)):
            key.append(key[x % len(key)])
        key = ''.join(key)
        return key

def enkripsivignere(plaintext, key):
    key = keygenerator(plaintext, key)

    plaintext = list(plaintext)
    enkripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                hurufawal = ord("A")
                convert = (ord(plaintext[x])- hurufawal) + (ord(key[x].upper()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                enkripsi.append(hasil)
            if plaintext[x].islower():
                hurufawal = ord("a")
                convert = (ord(plaintext[x])- hurufawal) + (ord(key[x].lower()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                enkripsi.append(hasil)
        else:
            enkripsi.append(plaintext[x])
        
    return  "".join(enkripsi)

def deskripsivignere(chipertext, key):
    key = keygenerator(chipertext, key)
    plaintext = list(chipertext)
    deskripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                hurufawal = ord("A")
                convert = (ord(plaintext[x])- hurufawal) - (ord(key[x].upper()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                deskripsi.append(hasil)
            if plaintext[x].islower():
                hurufawal = ord("a")
                convert = (ord(plaintext[x])- hurufawal) - (ord(key[x].lower()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                deskripsi.append(hasil)
        else:
            deskripsi.append(plaintext[x])

    return "".join(deskripsi)

def CheckMMI(keyA): 
    n = [1,3,5,7,9,11,15,17,19,21,23,25] 
    for i in n: 
        looping = (keyA * i) % 26 
        if looping == 1:
            return i
def EnkripsiAffine(plaintext, keyA,keyB): 
    hasil = [] 
    for x in plaintext: 
        if x.isalpha(): 
            if x.isupper(): 
                Type = ord("A") 
                perkata = ord(x) 
                operasi = perkata - Type 
                operasi1 = keyA*operasi+keyB 
                mod = operasi1 % 26 
                hasilakhir = chr(mod + Type) 
                hasil.append(hasilakhir)
            else:
                Type = ord("a")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = keyA*operasi+keyB
                mod = operasi1 % 26
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
        else: 
            hasil.append(x) 
    return ''.join(hasil)

def DeskripsiAffine(plaintext, keyA,keyB): 
    hasil = [] 
    y = CheckMMI(keyA) 
    for x in plaintext: 
        if x.isalpha():
            if x.isupper():
                Type = ord("A")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = y*(operasi-keyB)
                mod = operasi1 % 26
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
            else:
                Type = ord("a")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = y*(operasi-keyB)
                mod = operasi1 % 26 
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
        else:
            hasil.append(x)
    return ''.join(hasil) 

if math.gcd(keyA, 26) == 1: 
    print("==================")
    print("vigenere chiper")
    print("plaintext : " + plaintext)
    print("key : " + key)
    enkripsivignere = enkripsivignere(plaintext, key)
    enkripsiaff = EnkripsiAffine(enkripsivignere, keyA, keyB)
    print("enkripsi vig+Aff : " + enkripsiaff)

    print("affine chiper")
    print("key A : " + str(keyA))
    print("key B : " + str(keyB))
    deskripsiaff = DeskripsiAffine(enkripsiaff, keyA, keyB)
    deskripsivig = deskripsivignere(deskripsiaff, key)
    print("deskripsi : " + deskripsivig)
else: 
    print("Kunci A tidak bisa") 