import statistics as s 
#entrada
lote1 = int(input('Produção do primeiro lote: '))
lote2 = int(input('Produção do segundo lote: '))
lote3 = int(input('Produção do terceiro lote: '))
 
media = s.mean((lote1, lote2, lote3) )
desvio = s.stdev((lote1, lote2, lote3))
print(f'Média: {media: .2f}')
print(f'Desvio padrão: {desvio:.2f}')

 