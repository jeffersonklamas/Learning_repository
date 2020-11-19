# Trabalhar com pacotes, fazer request
# O que são pacotes
# O que é o instalador de pacotes Python (PIP)
# Como instalar um pacote Python
# como listar pacotes instalados no Python
# Como utilizar um pacote
# Instalar primeiro pacote (Requests)
# Realizar uma requisição http com requests

# pacotes no python, podem ser chamados de bibliotecas
# pacotes são bibliotecas que já possuem funcionalidades que facilitam a produção
# Para chamar um pacote vá no terminal e instale o mesmo através do pip install nome do pacote ou pipenv.
# Após instalar, para usar o pacote utilize a função import nome do pacote

import requests # importando o pacote requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)) # endereçando uma api para solicitação através do request
    print(response.status_code) # verificando se o request esta funcionando, 200  esta ok
    # print(response.text) # irá imprimir todo o texto da página, neste caso é a  página em jason
    print(response.json()) # irá trazer todo o conteúdo já em formato de dicionário
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
     response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
     dados_pokemon = response.json()
     return dados_pokemon
def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://digitalinnovation.one/')
    print(response)
#    retorna_dados_cep('83325190')
#     dados_pokemon = retorna_dados_pokemon('pikachu')
#     print(dados_pokemon['sprites'] ['front_shiny'])


