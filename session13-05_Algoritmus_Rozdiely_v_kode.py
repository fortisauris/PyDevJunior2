'''
A L G O R I T M U S  - P R I K L A D   R O Z D I E L Y   V  K O D E
'''

uzivatelia = [
    {"user": "jankoNeznamy", "vyska": 1.75},
    {"user": "mariaNeznama", "vyska": 1.68},
    {"user": "JankoEstemenejznamy", "vyska": 1.96},
]

# ZLY SPOSOB - PROCEDURALNY
najvyssi_user = ''
maximalna_vyska = 0

for user in uzivatelia:
    if user["vyska"] > maximalna_vyska:
        max_height = user["vyska"]
        highest_user = user

print(najvyssi_user, maximalna_vyska)

# DOBRY SPOSOB FUNKCIONALNY
najvyssi_user = max(uzivatelia, key=lambda user: user["vyska"])
print(najvyssi_user)

