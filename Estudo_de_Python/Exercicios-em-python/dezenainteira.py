# -----------------------------------------------------
# Exercício desenvolvido por Jefferson Klamas Maarzani
# Para as atividades do Curso da UFSCAR disponíveis na 
# Plataforma do Coursera para o curso de Introdução
# da Ciência da Computação com Python
# -----------------------------------------------------
#
# Enunciado
#
# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. 
def main():
    #Entrada de dados
    print("\n")
    valor = int(input("Digite um número inteiro: "))
    #Cálculo
    resultado = (valor // 10) % 10
    # Saída
    print("O dígito das dezenas é", resultado, "\n")
    print("Fim !!!")
    #Fim
main()