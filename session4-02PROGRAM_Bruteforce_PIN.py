import hashlib

def hash_it(text: str):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')  # ascii
    h.update(data)
    return h.hexdigest()

# BRUTEFORCE
for i in range(0, 10000):  # slabe heslo
    hashstring = hash_it(str(i))
    print(i, hashstring)
    if hashstring == '90ef635b07e4335585e9aa6c7d742e94':
        print('MAM TA JE TO ROZLUSKNUTE. HESLO JE :', i)
        quit()

# janka35  # SLABE HESLO

# V!9ra_som_v9c9ral_ryb0  # SILNE HESLO