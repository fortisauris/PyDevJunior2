# ROZCVICKA

# jednoduchy generator mesiacov

def generator_mesiacov():
    mesiace = ('jan', 'feb','mar','apr')  # tuple
    for i in mesiace:
        yield i

mes = generator_mesiacov()
for i in range(3):
    print(next(mes))

# januar, februar, marec ....

# zavolam generator a hodi mi dalsi mesiac v poradi

# iniciovat generator

# vytahovat hodnoty


# Vladov repozitar ---> https://github.com/Aberran/ReactionTime-PyGame.git
