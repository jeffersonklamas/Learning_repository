#TOPSIS R "NA MÃO"
#AULA DE 17/11/2020 da Casa da Pesquisa Operacional
#Tomada de Decisão Multicritério usando Método TOPSIS.
#Desenvolvedor em R Professor Thiago Marques

#Carregando a biblioteca
library(dplyr)
#install.packages("dplyr")

#Construindo a matriz de decisão
vetor_pesos = c(0.5, 0.3, 0.2)
vetor_alternativas = c("prov1", "prov2", "prov3")
vetor_criterios = c("custo","prazo","veloc")
valores = c(90, 20, 80, 120, 8, 100, 70, 12, 90)

dados = matrix(
  valores,
  dimnames = list(c("prov1", "prov2", "prov3"),
                  c("custo", "prazo", "veloc")),
  nrow = 3,
  ncol = 3,
  byrow = T
)

colnames(consolidado)=c("custo","prazo","veloc")
rownames(consolidado)=c("prov1", "prov2", "prov3")


#Normalizando a matriz de decisão
consolidado = cbind(
  dados[, 1] / norm(as.matrix(dados[, 1]), type = "2"),
  dados[, 2] / norm(as.matrix(dados[, 2]), type = "2"),
  dados[, 3] / norm(as.matrix(dados[, 3]), type = "2")
)

consolidado1.2 =
  data.frame(
    custo = dados[, 1] / sqrt(sum(dados[, 1] ^ 2)),
    bateria = dados[, 2] / sqrt(sum(dados[, 2] ^ 2)),
    camera = dados[, 3] / sqrt(sum(dados[, 3] ^ 2))
  )

#Confirmando se os resultados realmente são iguais:
consolidado1.2 - consolidado

#Arredondando
round(consolidado1.2 - consolidado)

#Ponderando a matriz normalizada pelo Peso
consolidado2 = cbind(vetor_pesos[1] * consolidado[, 1],
                     vetor_pesos[2] * consolidado[, 2],
                     vetor_pesos[3] * consolidado[, 3])

#se monotônicos de benefício max()
#se monotônicos de custo min()

#Criando a Solução Ideal Positiva (SIP)
vetor_A_mais = cbind(min(consolidado2[, 1]),
                     min(consolidado2[, 2]),
                     max(consolidado2[, 3]))

#Criando a Solução Ideal Negativa (SIN)
vetor_A_menos = cbind(max(consolidado2[, 1]),
                      max(consolidado2[, 2]),
                      min(consolidado2[, 3]))

#Criando a distância das alternativas propostas a Solução Ideal Positiva (SIP)
d_A_mais = cbind(
  dist(rbind(consolidado2[1, ], vetor_A_mais), method = "euclidean"),
  dist(rbind(consolidado2[2, ], vetor_A_mais), method = "euclidean"),
  dist(rbind(consolidado2[3, ], vetor_A_mais), method = "euclidean")
)

#Criando a distância das alternativas propostas a Solução Ideal Negativa (SIN)
d_A_menos = cbind(
  dist(rbind(consolidado2[1, ], vetor_A_menos), method = "euclidean"),
  dist(rbind(consolidado2[2, ], vetor_A_menos), method = "euclidean"),
  dist(rbind(consolidado2[3, ], vetor_A_menos), method = "euclidean")
)

#Cálculo da proximidade relativa

importancia_relativa_alternativa1 = d_A_menos[, 1] / (d_A_mais[, 1] + d_A_menos[, 1])
importancia_relativa_alternativa2 = d_A_menos[, 2] / (d_A_mais[, 2] + d_A_menos[, 2])
importancia_relativa_alternativa3 = d_A_menos[, 3] / (d_A_mais[, 3] + d_A_menos[, 3])

#Consolidando as importâncias relativas
consolidado_importancia = cbind(
  importancia_relativa_alternativa1,
  importancia_relativa_alternativa2,
  importancia_relativa_alternativa3
)

#Consolidando os resultados em uma matriz
consolidado_final = cbind(consolidado2, array(consolidado_importancia))

#Consolidando os resultados em um data.frame
consolidado_final = data.frame(consolidado_final)

#Renomeando
colnames(consolidado_final) = c(vetor_criterios, c("importancia_relativa"))

#Ordenando
consolidado_final_ordenado = consolidado_final %>% arrange(desc(importancia_relativa))

#Criando o resultado final dos rankings
consolidado_final_ordenado$Ranking = seq(1, by = 1, dim(consolidado_final)[1])

#Exemplo cbind

vetor1=c("pablo","thiago")
vetor2=c("Marcos","Julio")

rbind(vetor1,vetor2)

