# Transformar segundos em Horas

#Interatividade com o usuário.
segundos_str = input("Informe o número de segundos que quer converter: ")
segs_total = int(segundos_str)

# Desenvolvimento do cálculo

# Calcular as horas:
horas = segs_total // 3600 ## A divisão inteira
segs_restantes = segs_total % 3600 # o Resto da divisão
#Calcular os minutos:
minutos = segs_restantes // 60
segs_restantes_fim = segs_restantes % 60 

# Saída na Tela:

print("São", horas, "horas, ", minutos, "minutos e", segs_restantes_fim, "segundos.")