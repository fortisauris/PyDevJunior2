'''
ALGORITMUS NAJKRATSIA CESTA
'''

graph = dict()
graph['BA'] = ['TT']
graph['TT'] = ['BA', 'NR', 'PN']
graph['NR'] = ['TT','BB']
graph['PN'] = ['TT', 'TN']
graph['BB'] = ['KE', 'NR']
graph['TN'] = ['ZA', 'PN']
graph['KE'] = ['BB', 'PP']
graph['ZA'] = ['PP', 'TN']
graph['PP'] = ['KE', 'ZA']

def najkratsia_cesta(graph: dict, mesto1: str, mesto2: str):
    cesta_zoznam = [[mesto1]]
    cesta_index = 0

    predchadzajuce_mesto = {mesto1}
    if mesto1 == mesto2:
        return cesta_zoznam[0]

    while cesta_index < len(cesta_zoznam):
        aktualna_cesta = cesta_zoznam[cesta_index]
        posledne_mesto = aktualna_cesta[-1]
        dalsie_mesta = graph[posledne_mesto]

        if mesto2 in dalsie_mesta:
            aktualna_cesta.append(mesto2)
            return aktualna_cesta

        for dalsie_mesto in dalsie_mesta:
            if not dalsie_mesto in predchadzajuce_mesto:
                nova_cesta = aktualna_cesta[:]
                nova_cesta.append(dalsie_mesto)
                cesta_zoznam.append((nova_cesta))

                predchadzajuce_mesto.add(dalsie_mesto)
        cesta_index += 1
    return []

print(najkratsia_cesta(graph, 'BA', 'KE'))
print(najkratsia_cesta(graph, 'BA', 'NR'))

# TODO SKuste pouzit debugger