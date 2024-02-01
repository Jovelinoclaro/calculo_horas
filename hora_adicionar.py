
#importa a função date
from datetime import datetime, timedelta

#linha que faz input para o usuario digitar
hora_inicial_str = input('Digite hora no formato HH:MM: ')
hora_inicial = datetime.strptime(hora_inicial_str, "%H:%M")
#linha que faz inut dos minutos para digitar
minutos_str = int(input('Digite os minutos: '))
nova_hora = hora_inicial + timedelta(minutes=minutos_str)
#imprime na tela os minutos adicionados e a hora calculada
print(f'A nova hora após adicionar {minutos_str} minutos é: {nova_hora.time()}')
