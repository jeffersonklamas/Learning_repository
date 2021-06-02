# -----------------------------------------------------
# Exercício desenvolvido por Jefferson Klamas Maarzani
# Para as atividades do Curso da UFSCAR disponíveis na 
# Plataforma do Coursera para o curso de Introdução
# da Ciência da Computação com Python
# -----------------------------------------------------
#
# Enunciado
# Dada a quantidade de segundos, "quebre" esse valor em dias, horas,
# minutos e segundos. A saída deve estar no formato: a dias, b horas,
# c minutos e d segundos. 
#
# Transformar segundos em Horas
#
#Interatividade com o usuário.
seconds = input("Informe o número de segundos que quer converter: ")
total_seconds = int(seconds)
#
# Desenvolvimento do cálculo
#
# Calcular os dias:
days = total_seconds // 86400
left_seconds = total_seconds % 86400
# Calcular as horas:
hours = left_seconds // 3600
left_seconds2 = left_seconds % 3600
#Calcular os minutos:
minutes = left_seconds2 // 60
final_seconds = left_seconds2 % 60
# Saída na Tela:
print(days, "dias,", hours, "horas,", minutes, "minutos e", final_seconds, "segundos.")
#Fim
