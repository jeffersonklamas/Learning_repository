# -----------------------------------------------------
# Exercício desenvolvido por Jefferson Klamas Maarzani
# Para as atividades do Curso da UFSCAR disponíveis na 
# Plataforma do Coursera para o curso de Introdução
# da Ciência da Computação com Python
# -----------------------------------------------------
#
# Enunciado
#
# Escreva um programa que receba (entrada de dados através do teclado)
# o nome do cliente, o dia de vencimento, o mês de vencimento e o valor
# da fatura  e imprima (saída de dados) a mensagem com os dados recebidos,
# no mesmo formato da mensagem acima. Note que o programa imprime a saída
# em duas linhas diferentes. Note também que, como não é preciso realizar
# cálculos, o valor não precisa ser convertido para número, pode ser
# tratado como texto.
#
# Entrada de dados:
nomecliente = input("Informe o nome do cliente: ")
datavencimento = input("Data de vencimento da fatura: ")
mesvencimento = input("Mês do vencimento da fatura: ")
valordafatura = input("Valor da fatura: ")
# Desevolvimento
print("Olá,",nomecliente)
print("A sua fatura com vencimento em", datavencimento,"de",mesvencimento,"no valor de R$", valordafatura,"está fechada.")
# Fim