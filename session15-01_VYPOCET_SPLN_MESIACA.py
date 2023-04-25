import datetime

# terajsi datum a cas => datetime.datetime.now()
teraz = datetime.datetime.now()

# termin najblizsieho splnu   5.5.2023 19:34  #
spln = datetime.datetime(year=2023, month=5, day=5, hour=19, minute=34)

# datetime.timedelta() # zobrazovat na obrazovke  # CASOVY USEK
cas_do_splnu = spln - teraz
# odpocet sa nam zobrazi ako timedelta object
print(cas_do_splnu)


# ADVANCED... vypocitat dalsi spln ... 29.5 dna od posledneho splnu