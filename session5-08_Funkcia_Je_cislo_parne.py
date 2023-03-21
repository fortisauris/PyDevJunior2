
def je_cislo_parne(n: int) -> bool:
    if n/2 == int(n/2):
        return True
    else:
        return False


for i in range(50):
    print(i, je_cislo_parne(i))
