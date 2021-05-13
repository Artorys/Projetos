nome = str(input('Digite seu nome'))
idade = int(input('Digite sua idade'))
salario_base = float(input('Digite seu salário inicial'))


if idade >=30 and idade <=60:
 reajuste = salario_base * 30 / 100 # Aumento de 30%
 reajuste1 = reajuste + salario_base

 print(f'parabéns {nome} ,você recebeu um aumento de 30%,\n seu salário atual é {reajuste1} !')


elif idade >= 20 and idade <30:

 reajuste2 = salario_base * 20/100#Aumento de 20%
 reajuste3 = reajuste2 +salario_base

 print (f'parabéns {nome} ,você recebeu um aumento de 20%,\n seu salário atual é {reajuste3}')


elif idade <18:

    print('você n tem idade para trabalhar')
else:
    print('você n tem idade para trabalhar!')

