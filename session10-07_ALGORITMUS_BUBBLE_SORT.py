'''
sort, sorted  uz pozname
SORTOVANIE BBBLE SORT
'''

def bubble_sort(zoznam: list):
    dlzka = len(zoznam)
    for i in range(dlzka):
        uz_zoradene = True  # flag

        for j in range(dlzka - i - 1):
            if zoznam[j] > zoznam[j+1]:
                zoznam[j], zoznam[j+1] = zoznam[j+1], zoznam[j]  # vymenime poradie
                uz_zoradene = False  # zmenime zastavku na False
        if uz_zoradene:  # uz_zoradene is True
            break
    return zoznam # vratime zoradeny zoznam


z = [543,543,6757,65,7865,876,8765,73,67657,68768,6564]
print(bubble_sort(z))


