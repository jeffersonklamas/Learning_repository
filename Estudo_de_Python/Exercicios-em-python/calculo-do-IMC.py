# Cálculo para saber o valor do IMC do usuário.
def main():
    
    print("Cálculo para saber o valor do IMC ")


    print("\nIMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa.")
    print("\nO índice é calculado da seguinte maneira: divide-se o peso do solicitante pela sua altura elevada ao quadrado. Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.\n")

    # print("Interpretação do IMC")
    # print("IMC Classificação Obesidade (Grau))
    # print("MENOR QUE 18,5	MAGREZA	0")
    # print("ENTRE 18,5 E 24,9	NORMAL	0")
    # print("ENTRE 25,0 E 29,9	SOBREPESO	I")
    # print("ENTRE 30,0 E 39,9	OBESIDADE	II")
    # print("MAIOR QUE 40,0	OBESIDADE GRAVE	III")"

    print("Use pontos para separar os valores. Exemplo: 1.66 \n")
    altura = float(input("Digite sua altura: "))
    peso = int(input("Digite o seu peso: "))

    #Desenvolvendo os cálculos
    #Conforme a OMS o indice é calculado da seguinte maneira: divide-se o peso
    # do solicitante pela sua altura elevada ao quadrado.

    resultadoinicial = float(peso / (altura ** 2))

    print(resultadoinicial)


    # Implementar a interpretação do IMC, conforme tabela da OMS.
    # if resultadoinicial < 18.5{
    #    print("O seu valor do seu IMC é {} considerado magro".format(resultadoinicial))
    #) if resultadoinicial <= 24.9(
    #    print("O seu valor do IMV é {} considerado normal".format(resultadoinicial))
    #} """
main()

