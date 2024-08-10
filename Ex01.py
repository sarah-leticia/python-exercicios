salarioBruto =  float(input('Qual o valor do salario?'))
porcentagem = int(input('Qual a porcentagem de aumento?'))
percentual = porcentagem/100
aumento = salarioBruto*percentual
SalarioAtual = salarioBruto+aumento
print('o valor do aumento é de R$ {}. E o novo valor do salario é: R$ {}' 
      .format(aumento, SalarioAtual ))