mariana = 2 # Dona da casa
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
participantes = len(dedos)
somadedos = sum(dedos)
dedoapontados = 0
for x in range(somadedos):
    if dedoapontados > participantes:
        dedoapontados = 0
    dedoapontados +=1
dedos = list(dedos)
print('Foi apontado para: {}.'.format(dedos[dedoapontados]))