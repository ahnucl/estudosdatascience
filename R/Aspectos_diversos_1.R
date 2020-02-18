getwd()
#setwd("C:\\Workspace - Estudos/Data/R/")

iristeste = iris
save(iristeste, file="iristeste.RData")
rm(iristeste) # remove da memória
iristeste
load(file="iristeste.RData")

x = c(12,34,56,79)
y = c(1,6,9,14)

plot(x,y)
rm(x,y)

quit()
