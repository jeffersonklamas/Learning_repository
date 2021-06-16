#-----------------------------------
# Métodos utilizados com strings em Python
#
#------------------------------------
#
print("\nLower(), retorna uma versão da string em caracteres minúsculos\n")
b = "TEXTO DIGITADO SERÁ ALTERADO PELO MÉTODO LOWER"
print("\nTexto original\n")
print(b)
b = b.lower()
print("\nTexto alterado\n")
print(b,"\n")
#Fim deste método

print("\nMétodo replace(), irá substituir um trecho de uma string por outro\n")
b = b.replace("será alterado", "alterado")
print(b,"\n")
#Fim deste método

print("\nMétodo count(), retorna o número de ocorrências de uma substring na string\n")
c = b.count('a')
print(c)
#Fim deste método

print("\nMétodo split(), divide uma string em partes definidas por um marcador e retorna um array\n")
b = b.split(" ")
print(b,"\n")
#Fim deste método

print("\nMétodo join(), transforma um array de strings em apenas uma string")

array1 = ["hoje", "é", "um", "excelente", "dia"]
print("\nDicionário original\n")
print(array1,"\n")
f = " ".join(array1)
print("\nUtilizando o método join para formar uma única string\n")
print(f,"\n")
#Fim deste método

print("\nMétodo strip(), retira espaços de início e do fim de uma string")

umastring = "     Olá     "
print(umastring,"\n")
umastring = umastring.strip()
print(umastring,"\n")


"""
print("\nMétodo strip(), Exclui os espaços do início e o dim de uma string\n")
novo = novoa.strip()
print(novoa,"\n")

"""