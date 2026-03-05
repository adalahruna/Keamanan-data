def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def mod_inverse(e,phi):
    for d in range(1,phi):
        if (e * d) % phi == 1:
            return d
    return None

print("=== KEY GENERATION ===")

p = 61
q = 53
print("Bilangan prima p:", p)
print("Bilangan prima q:", q)

n= p * q
print("Nilai n (p*q):", n)

phi = (p -1) * (q -1 )
print("Nilai phi:", phi)

e = 17
print("Nilai e:", e)

if gcd(e,phi) != 1:
    raise Exception("Error: e Tidak relatif prima dengan phi")

d = mod_inverse(e,phi)
print("Nilai d(mod inverse):",d)

print("\nPublic Key (e,n):", (e, n))
print("\nPrivate Key (d, n):", (d,n))

def encrypt(plaintext, e, n):
    cipher = []
    print("\n=== Proses Enkripsi ===")
    for char in plaintext:
        m = ord(char)
        print(f"Huruf: {char} -> ASCII:", m)
        
        c = pow(m, e, n)
        print(f"Enkripsi: {m}^{e} mod {n} =", c)
        
        cipher.append(c)
    return cipher

def decrypt(ciphertext, d, n):
    plain = ""
    print("\n=== proses Dekripsi ===")
    for c in ciphertext:
        print("Cipher:", c)
        
        m = pow(c, d, n)
        print(f"Dekripsi: {c}^{d} mod {n} =",m)
        
        char = chr(m)
        print("Kembali ke huruf:", char)
        
        plain += char
    return plain


print("\n=== Demo ===")
message = input("Masukkan pesan:")

ciphertext = encrypt(message, e, n)
print('\nCiphertext:', ciphertext)

decrypted_message = decrypt(ciphertext, d, n)
print("\nHasil Dekripsi;", decrypted_message)