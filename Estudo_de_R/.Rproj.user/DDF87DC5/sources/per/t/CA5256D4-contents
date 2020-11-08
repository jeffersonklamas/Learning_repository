#### Iniciando Estudos em R conceitos básicos 

# Principais operações matemáticas no R

2*2-(4/4)/2

1+1 # adição
4-2 # Subtração
6*9 # Multiplicação
4/2 # Divisão
3^2 # Potência
1751 %% 3 # Resto da divisão de 1751 por 3 
1751 %/% 3 # Parte inteira da divisão de 1751 por 3

# LEMBRE: as operações e suas precedências são mantidas como na matemática, 
# ou seja, divisão e multiplicação são calculadas antes da adição e subtração.
# Os parênteses são importantes e nunca é demais.

# Criando e aprendendo sobre tipos de variáveis e Objetos em R

# Primeiro objeto: Vetores
# A primeira coisa a ser feita é dar nome ao objeto que se irá criar, lembre da Syntax do R
# Sem espaços, sem caracterese especiais, não usar os comandos principais (ver manual),
# O R é Case-sensitive, ou seja, Ele diferencia Maiúsculo de Minúsculo, 
# Comandos basicos do R, após criar o objeto para se gravar a informação de valor o comando 
# pode ser, Dependendo da versão do R:
# 1. Selecionar a linha completa e pressionar Run no canto superior direito do editor.
# 2. Ir no inicio da linha ou ao final da linha e pressionar as teclas Ctrl+Enter

# numeric
#       neste exemplo criei o objeto preco e utilizei o sinal de atribuição <- poderia ter
#       usado o sinal de =, mas no R geralmente se usa o sinal de atribuição <-
#       A letra c que aparece após o sinal de atribuição é para informar ao R que estou
#       concatenando a informação.
#       Para separar os números no R se usa o sinal de ponto.
#       Tecla de atalho para o sinal de Atribuição <- 
#       pressione Alt - ( pressione a tecla Alt mais o sinal de menos)
#       Outra dica de tecla de atalho, vai usar muito o operador pipe ( %>% )
#       pressione as teclas Ctrl Shift m ( pressione as teclas Ctrl mais Shift mais a letra m)

preco <- c(16.92, 24.03, 7.61, 1.49, 11.77)
View(preco)

# A função str() informa o tipo de objeto se é numeric, string, factor)
str(preco)

# numeric

custo <- c(5.30, 6.95, 132.02, 75.50, 6.53)
View(custo)
str(custo)

# Character

produto <- c('M', 'M', 'O', 'P', 'P')
produto
str(produto)

# factor
# A função factor() vai converter um vetor de texto ou numerico para factor, ou seja,
# Vai ser usado para equiparar os valores, muito usado em modelo de regressão, a função factor
# vai realziar esta comparação.

produto <- factor(produto)
produto

# bolean
# vetor boleano, valores lógicos (verdadeiro ou falso)
# Neste exemplo estou informando ao R que com relação ao preço X custo, informo se 
# é verdadeiro ou falso, se o custo for mais baixo que o valor de venda, então tive lucro (TRUE)
# se o custo for mais alto que o valor de venda, então tive prejuizo (FALSE)

lucro_obteve <- c(TRUE, TRUE, FALSE, FALSE, TRUE)
sum(lucro_obteve)

# Date
# No R para que o mesmo possa identificar a data inclua o comando as.Date com o D em maiúsculo
datas <- as.Date(c('2020-05-15', '2020-05-16', '2020-05-17', '2020-05-18', '2020-05-19'))

# Comparando dois vetores
preco > custo

# Instalação de pacotes
# no Rstudio é possível instalar de duas maneiras indo no menu Packages
# e pesquisar se já possui o pacote, caso negartivo, clicar em install e informar
# o nome do pacote.
# A outra maneira é realizar a instrução abaixo: sendo que o nome entre aspas 
# é o pacote que será baixado.

install.packages('dynlm')

# As vezes pode ocorrer algum erro, tente
install.packages('dynlm' , dependencies = t)

# Para usar as funções do pacote, use a instrução abaixo.

library(dynlm)
#ou
require(rpart)

#Aprendendo a Importar bases em formato excel e csv.
# Lembre a tela do Rstudio possui 4 quadrantes:
# Quadrante Editor: Onde se digita o código (Tela superior a esquerda)
# Quadrante Console: Onde se roda os códigos e é apresentado as saídas (Tela inferior a esquerda). [A casa do R é neste quadrante]
# Quadrante environment: Painel com todos os objetos criados na sessão. (Tela superior a direita)
# Quadrante Output: Subdividido em 5 minis-abas. (Tela inferior a direita)
# Subdivisão do quadrante Output:
# Files: Mostra os arquivos no diretório de trabalho.
# Plots: Painel onde os gráficos são apresentados.
# Packages: Lista de pacotes instalados e onde se pede para instalar novos pacotes e update.
# Help: Painel para documentação de consultas das funções.
# Viewer: painel com histórico dos comandos rodados.

# Consulte o site para melhor visualização: https://www.curso-r.com/material/rstudio/#header-introducao

# para importar um arquivo no RStudio acesse a opção import Dataset no quadrante environment
# e informe o tipo de arquivo a ser carregado, na aba que abre informe o diretório onde esta o arquivo
# pode definir a aba que será aberta em sheet, será apresentado uma pré visualização de enter e pronto.
# ou use o comando abaixo para que o mesmo possa abrir diretamente o arquivo.
# lembre o meu é um exemplo, terá que inserir o caminho correto do seu arquivo.

library(readxl)
BD_marcas_de_chocolate <- read_excel("~/Documentos/Aula_Marketing_Analytics_Estatidados/BD_marcas_de_chocolate.xlsx")
View(BD_marcas_de_chocolate)

# O mesmo vale para abrir arquivos em csv, é importante antes abrir seu arvuivo csv para conhecer os detalhes do mesmo.
# pode haver alguns erros que podem solucionados ao visualizar seu csv antes.

