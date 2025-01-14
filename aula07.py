#Calculando IMC

nome = input(f'Qual o seu nome?')

altura = float(input(f'Qual a sua altura em metros?'))

peso = float(input(f'Qual o seu peso em quilos?'))

imc = peso / (altura*altura)

print(f'\n{nome}, seu IMC é {imc:.2f}.')

if imc <= 18.5:
    print(f' voce está abaixo do peso, alimente-se melhor!')
elif imc <= 24.9:
    print(f' seu peso esta ideal. Parabéns')
elif imc <= 29.9:
    print(f' voce está acima do peso. pratique exercícios e alimente-se melhor!')
elif imc <= 34.9:
    print(f'Você está com obesidade grau I. Cuide de sua saúde!')
elif imc <=39.9:
    print(f'Você está com obesidade grau II. Consulte um profissional de saúde.')
else:
    print(f'Você está com obesidade grau III (mórbida). É essencial buscar ajuda médica.')        