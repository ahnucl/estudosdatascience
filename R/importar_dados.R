# texto:
x = read.csv(file.choose(), header = T, sep = ";")
x

# odbc
install.packages("RODBC")
library(RODBC)

conexao <- odbcDriverConnect('driver={SQL Server};server=DESKTOP-UD9RQJ9\\SQLEXPRESS;database=VENDAS;trusted_connection=true')
# parâmetros usados na aula

resultado <= sqlQuery(conexao, "select * from dbo.vendas")

resultado

odbcClose(conexao)

# planilha
install.packages("xlsx")
library(xlsx)
dados = read.xlsx(file.choose(), sheetIndex = 1) # exemplo da aula, não tenho nenhuma planilha assim para testar
dados

# arff
install.packages("foreign")
library(foreign)
dados2 = read.arff(file.choose())
dados