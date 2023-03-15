# Textovy retazec STRING

text = str()
print(text)
text = ""
text += "Toto som teraz vymyslel. teraz"
print(text)
print('teraz' in text)
vysledok = "teraz" in text
print(vysledok)
print(len(text))  # dlzka textoveho retazca - STRINGU

print(text.upper())
print(text.lower())
print(text.islower())

print(text.count("teraz"))
print(text.split('.'))  #   Vystup z tohoto bude ZOZNAM v Python list  []

text += "\n\t" + "Ahojte" + " Andrej"
print(text)

# text -= "teraz"  # TODO TOTO NEFUNGUJE
print(text[0])
print(len(text))
print(text[0:5])
print(text[10:15])
print(text[15])
print(text[-6:])
