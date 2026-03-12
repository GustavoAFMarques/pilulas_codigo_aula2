import datetime as d
#entradas
data_compra = input('Digite a data da compra d/a/aaaa: ') 
prazo_garantia = int(input('Prazo de garantia: '))

#processamentos
data_inicial = d.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + d.timedelta(days= prazo_garantia * 30)

#saida
print(f"Data de termino: {data_final.strftime('%d/%m/%Y')}")
print(f"Dia da semana: {data_final.strftime('%A')}")