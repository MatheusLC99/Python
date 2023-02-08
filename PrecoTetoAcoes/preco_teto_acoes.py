ticker = input('Digite o nome do Ticker: \n')
print(ticker.upper())

lucro1 = int(input('\nLucro ano 1: \n'))
lucro2 = int(input('\nLucro ano 2: \n'))
lucro3 = int(input('\nLucro ano 3: \n'))
lucro4 = int(input('\nLucro ano 4: \n'))
lucro5 = int(input('\nLucro ano 5: \n'))
lucro6 = int(input('\nLucro ano 6: \n'))

medialucro = (((lucro1)+(lucro2)+(lucro3)+(lucro4)+(lucro5)+(lucro6))/6)

totalpapel = int(input('\nTotal de papel: \n'))

lpa = medialucro/totalpapel

pout = float(input('\nPayout(em decimais) medio (5 anos): \n'))

dpa = lpa*pout

vteto = dpa/(6/100)

print('\nO valor teto para ', ticker.upper(),'é R$:',vteto,'\n')