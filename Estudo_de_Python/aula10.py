# Aprendendo a manipular data e hora
# Realizar conversão de texto para data e vice versa
# Realizar soma e subtração em datas

# Recuparar a data atual (DATE)
# Trabalhando com data, alterando sua formatação
# Gerando um horário (TIME)
# Retornando data e hora atual (DATETIME)
# Realizando soma e subtração de datas com (TIMEDELTA)

# Data atual
# Existe um dicionário do python que ionforma o significado de sigla e seu retorno em tela dos comandos de data
from datetime import date, time, datetime, timedelta # declarando as funções no início para que se possa ser chamdo em todo arquivo

# data_atual = date.today()
# #print(data_atual) # traz a data atual em formato americano
# #print(data_atual.strftime('%d/%m/%y')) # retornando a data em formato brasileiro só com os dois últimos representando o ano
# # print(data_atual.strftime('%d/%m/%Y')) # Esta instrução tras a data o mês e o ano completo
# data_atual_str = data_atual.strftime('%A %B %Y') # Convertendo em string
# print(type(data_atual))
# print(data_atual_str)
# print(type(data_atual_str))

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=23, minute=59, second=30) # Com esta instrução é possível criar um horário
    print(horario)
    horario_str = horario.strftime('%H:%M:%S') # Por default o python já vai trazer em formato de horas separado por dois ponto, mas, se quiser declarar também é possível
    print(horario_str)

def trabalhando_com_datetime(): # com datetime é possível trazer separadamente as datas, mes, ano, dia separadamente.
    data_atual = datetime.now()
    print(data_atual) # mostrando data e hora atual, em formato americano com milessegundos
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) # Transformando em string, formato brasileiro, sem milessegundos
    print(data_atual.strftime('%c')) # Esta instrução traz o dia da semana, seguido do mês e data, bem como as horas seguidas do ano.
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo') # Criando uma tupla para traduzir para o portugues do brasil
    print(tupla[data_atual.weekday()])
    data_criada = datetime(1969, 3, 30, 17, 45, 59) # Criando uma data
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '30/03/1969 16:45:01' # transformando uma data de string para datetime
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=3, minutes=30, seconds=20) # fazendo calculo de subtração de data e horas
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=3, minutes=30, seconds=20) # Somando datas
    print(nova_data)
if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()