# -----------------------------------------------------
# Exercício desenvolvido por Jefferson Klamas Maarzani
# Para as atividades do Curso da UFSCAR disponíveis na 
# Plataforma do Coursera para o curso de Introdução
# da Ciência da Computação com Python
# -----------------------------------------------------
#
# Enunciado
# Faça um programa em Python que receba quatro notas,
# calcule e imprima a média aritmética. 
# Observe o exemplo abaixo:
#
# Exemplo:
#
# Entrada de Dados:
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
# Saída de Dados:
# A média aritmética é 5.5
#
nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
nota4 = int(input("Digite a quarta nota:"))
#Calculo
mediatotal = (nota1+nota2+nota3+nota4)/4
# saída
print("A média aritmética é", mediatotal)
# Fim