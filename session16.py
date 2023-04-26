# ROZCVICKU


# jednoduchy generator mesiacov

def generator_mesiacov():
    mesiace = ('jan', 'feb','mar','apr')  # tuple
    for i in mesiace:
        yield i

mes = generator_mesiacov()
for i in range(15):
    print(next(mes))

# januar, februar, marec ....

# zavolam generator a hodi mi dalsi mesiac v poradi

# iniciovat generator

# vytahovat hodnoty




