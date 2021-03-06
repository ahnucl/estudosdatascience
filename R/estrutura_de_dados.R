X <- c(2,5,1,"sa", "asdasd",2L)
X
X[4] <- 1000
X[1,1]

# lembrar como carrega o data frame iris
library(datasets)
iris[1,1]
iris$Species

#  Estruturas de Dados em R:

#  Vetores
#  Matrizes
#  Data Frames
#  Listas
#  Fatores -> vari�veis categ�ricas

# Estrutura de dados se aplicam sempre que trabalhamos com conjuntos de dados

# Matrizes

VADeaths # tem nomes em colunas e linhas
colnames(VADeaths) #
rownames(VADeaths)

# s� a terceira linha
VADeaths[3,]

# s� a segunda coluna
VADeaths[,2]

# Colunas da 2 a 4
VADeaths[,2:4]

# Linhas da 1 a 3
VADeaths[1:3,]

### Data Frames

class(longley) # data.frame
# mesmo uso das matrizes
longley[1:3,]

# Usando $
longley$Armed.Forces # resultado na horizontal
longley["Armed.Forces"] # resultado melhor estruturado (vertical)


### Listas
ability.cov
class(ability.cov)

ability.cov$cov # acesso pelo $
ability.cov[1] # acesso pelo �ndice
class(ability.cov$cov)

ability.cov$center
ability.cov[2] # acesso pelo �ndice
class(ability.cov$center)

ability.cov$n.obs
ability.cov[3]
class(ability.cov$n.obs)

# como o "cov" dentro de "ability.cov" � uma matriz, � poss�vel 
# usar a mesma sintaxe 
ability.cov$cov[,2:3]

### Fatores
# vari�veis categ�ricas com um n�mero limitado de valores diferentes
# s�o armazenados como inteiros

class(state.region)

state.region # levels diz quais o valores fixos
state.region[1]

# mudando o levels
teste <- state.region
class(teste)
levels(teste) <- c("Nordeste", "Sul", "Norte", "Centro", "Oeste")

teste


survey_vector <- c("M", "F", "M", "F", "F")
factor_survey_vector <- factor(survey_vector)
factor_survey_vector
survey_vector
levels(factor_survey_vector)
levels(factor_survey_vector) <- c("Feminino", "Masculino")

