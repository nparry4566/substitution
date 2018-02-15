alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321!@#$%^&*()_+=-\\][|}{';:/.,?><`~\""
key = " poiuytrewqasdfghjklmnbvcxzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321!@#$%^&*()_+=-\\][|}{';:/.,?><`~\""

def encrypt(string):
    new = ""
    for c in string:
        new += key[alphabet.find(c)]


    return new

def decrypt(string):
    new = ""
    for c in string:
        new += alphabet[key.find(c)]

    return new

msg = "big red dog"
encrip = encrypt(msg)
decrip = decrypt(encrip)


print(msg)
print(encrip)
print(decrip)
