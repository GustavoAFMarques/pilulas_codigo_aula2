import locale as l
l.setlocale(l.LC_ALL, 'pt_BR.UTF-8' )

receita1 = int(input('Valor do mes de julho: '))
receita2 = int(input('Valor do mes de agosto: '))
receita3 = int(input('Valor do mes de setembro: '))

total = receita1+receita2+receita3
print(f'Mes 1: {l.currency(receita1, grouping=True)}')
print(f'Mes 2: {l.currency(receita2, grouping=True)}')
print(f'Mes 3: {l.currency(receita3, grouping=True)}')
print(f'Total: {l.currency(total, grouping=True)}')








