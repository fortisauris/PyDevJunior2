import hashlib

def hash_it(text: str):
    h = hashlib.md5()
    data = bytes(text, encoding='utf8')  # ascii
    h.update(data)
    return h.hexdigest()


# HLAVNY PROGRAM
hashstring = hash_it('7567')
print(hashstring)