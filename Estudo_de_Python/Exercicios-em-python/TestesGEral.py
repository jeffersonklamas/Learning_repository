""" a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print("O valor de a é",a)
print("O valor de b1 é",b)

s = 0
for d in range(0, 5, 0.1):
    s += d
    print(s)
    
a = 60
b = 30
c = b if (b > a) else a
print(b)
print(c)

x = 67
y = 80
x, y, z =1,2,3
print(x,y,z)

import re
c = "visite a pagina usando python"
print(re.findall(r"\w+",c))
print(re.findall(r"\d+",c))
print(re.findall(r"\s+",c))
print(re.findall(r"\b+",c))

a = 15
b = 15
print ('% x, % X' % (a,b)) # Não entendi a resposta f, F

a = "python"
b = "pythoN"
print (a > b)

import pywhatkit
pywhatkit.text_to_handwriting("Arquetipos como padrao de comportamento, segundo Jung. Ao que tudo indica, o criador do termo arquetipo foi o psicologo suiço Carl Jung. Para ele, arquetipos sao imagens primordiais, presentes em nosso imaginario, que ajudam a explicar historias passadas, vividas por outras geraçoes.", rgb=(0,0,255))


list = ["a","b","c"]
list.pop() # pop remove a última
print(list)

i = 1
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i)  


d = {0:'a', 1:'b', 2:'c'}
for x in d.keys():
    print(d[x])
 
idade = 16  
    
if (idade < 18): 
       print ("Não pode tirar carteira de habilitação")
else:
       print ("Pode tirar a carteira de habilitação")
"""

a = 0
b = 2
c = 1

if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
        print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")
