
'''
PALINDROM Slovo, ktore je rovnake odporedu aj odzadu
'''

def palindrome(slovo: str) -> bool:
    for i in range(len(slovo)):
        t = slovo[:i] + slovo[i+1:]
        if t == t[::-1]:
            return True
    return False

s = 'KOROK'
print(palindrome(slovo=s))
