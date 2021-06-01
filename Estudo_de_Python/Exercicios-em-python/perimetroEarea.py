# -----------------------------------------------------
# Exercício desenvolvido por Jefferson Klamas Maarzani
# Para as atividades do Curso da UFSCAR disponíveis na 
# Plataforma do Coursera para o curso de Introdução
# da Ciência da Computação com Python
# -----------------------------------------------------
#
# Enunciado
#
# Faça um programa em Python que receba (entrada de dados)
# o valor correspondente ao lado de um quadrado, calcule e
# imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"
# 
# Entrada de dados
lado=int(input("Digite o valor correspondente ao lado de um quadrado:"))
# Cálculo
pquadrado=(lado*4)
areaquadrado=(lado**2)
# Saída de Dados
print("perímetro:", pquadrado,"- área:", areaquadrado)
