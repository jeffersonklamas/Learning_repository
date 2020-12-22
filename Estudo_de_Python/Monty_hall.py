"""
Simulação: O problema de Monty Hall
#Suponha que você esteja participando de um jogo com três portas e que atrás de uma delas tenha um carro como prêmio.
#O apresentador do jogo pede a você que escolha uma porta. Se você escolher a porta que tem o carro, você ganha
#o carro.

#Entretanto, após você escolher sua porta, o apresentador abre uma outra porta do jogo e mostra que aquela porta 
#contém um bode. O apresentador, então, pergunta: “Você quer mudar de porta?”. 
#Há apenas duas portas sobrando, aquela que você escolheu primeiro e aquela que não foi aberta.
#
#Você mudaria de porta? Qual a probabilidade de você ganhar o prêmio, se mudar de porta?
"""
import numpy as np
from matplotlib import pyplot as plt
import random
from random import seed
seed(100)

portas = [1,2,3]
Nmax = 2000
P = []  # armazena a fração de vitórias
vN = [] # armazena o numero de jogos
for N in np.arange(1, Nmax, 10):
    vitoria = 0
    derrota = 0
    for i in range(0,N):
        C = random.choice(portas) # coloca o carro em uma porta
        X = random.choice(portas) # seleciona uma porta
        if(C != X): # se carro não está na porta selecionada
                    # o apresentador irá abrir outra porta que tem o animal
                    # Trocando a porta, ganha-se o carro.
                    vitora = vitoria + 1
    P.append(vitoria/N)
    vN.append(N)
plt.figure(figsize=(12,8))
plt.plot(vN, P, 'ro-', label='Simulação: Muda a porta')
plt.axhline(y=2/3,color='red', label='Prob. teórica com mudança de porta')
plt.ylim(0,1.05)
plt.legend()
plt.show(True)
