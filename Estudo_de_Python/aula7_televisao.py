# criando uma classe para implementar um canal

class Televisao:
    def __init__(self):
        self.ligada = False # toda vez que se inicia uma televisão, ela esta desligada
        self.canal = 2 # inicia o canal da televisão em 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

# criando a função para ir mudando de canal

    def aumenta_canal (self):
        if self.ligada:     # Ligando a televisão
            self.canal += 2 # aumenta o canal com mais um
    def diminui_canal (self):
        if self.ligada:     # ligando a televisão
            self.canal -= 1 # diminui o canal.
if __name__ == '__main__': # inserindo esta instrução para que caso haja a necessidade de se trabalhar com módulo e fazer testes, via terminal

    televisao = Televisao()
    print('A televisão está ligada? {}'.format(televisao.ligada))
    televisao.power() # Aqui vai ligar a televisão
    print('A televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('A televisão está ligada? {}'.format(televisao.ligada))
    #
    print ('Esta no Canal: {}'.format(televisao.canal)) # inicia o canal da tv, neste caso setado no canl 2
    televisao.power() # ligando a televisao
    print('A televisão está ligada? {}'.format(televisao.ligada))
    televisao.aumenta_canal() # aumenta o canal uma vez
    televisao.aumenta_canal() # aumenta o canal pela segunda vez
    print('Agora o Canal é: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal, agora é: {}'.format(televisao.canal))