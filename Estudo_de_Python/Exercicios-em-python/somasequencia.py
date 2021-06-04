
def main():
    print("\nDigite 0 (zero) para sair")
    num = int(input("Digite um inteiro: "))
    soma = 0

    while num != 0:
        soma1 = soma + num
        num = int(input("Digite um inteiro: "))

    print("A soma eh", soma1)


#----------------------------------------------
main()
