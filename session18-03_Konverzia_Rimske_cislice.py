
# ROZCVICKA  KONVERZIA RIMSKYCH CISLIC NA ARABSKE

def zmen_na_cislo(rimske_cislo: str) -> int:

    vysledok = int()
    if len(rimske_cislo) == 1:
        if rimske_cislo == 'I':
            return 1
        if rimske_cislo == 'V':
            return 5
        if rimske_cislo == 'X':
            return 10

    elif len(rimske_cislo) == 2:
        pass
        # I V X  a kto chce tak MDCL
        # od I do X

    return vysledok

print(zmen_na_cislo('X'))

# TODO Domaca uloha spravit komplet konverziu na z rimskych cisel na arabske
