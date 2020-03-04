teste1 <- function(){
  for(i in 2:6){
  print(i)
  }
  return = 10
}

x = teste1()

x
a = 99

if(a > 10)
{
  print("A maior que 10")
}else # se não for na chave o R vê um erro
{
  print("A não é maior")
}

x = ifelse(a < 100, "asdasd", "fffffff")
x


while(a > 20){
  print(a)  
  a <- a - 1
}
 