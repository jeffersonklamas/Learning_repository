#------------------------------------
# Criando texto png com a biblioteca pywhatkit
# Aprendendo a usá-la.
# No momento a mesma não aceita palavras acentuadas.
# Para uso ler a documentação referente a biblioteca.
# 
# Tutorial visto no instagram usuário @python.hub
#
# baixei a biblioteca via sudo pip install pywhtkit
# 
#------------------------------------

import pywhatkit
pywhatkit.text_to_handwriting("Arquetipos como padrao de comportamento, segundo Jung. Ao que tudo indica, o criador do termo arquetipo foi o psicologo suiço Carl Jung. Para ele, arquetipos sao imagens primordiais, presentes em nosso imaginario, que ajudam a explicar historias passadas, vividas por outras geraçoes.", rgb=(0,0,255))