#Escreva um programa que leia o ano de nascimento do usuário e retorne quantos anos ele fará em 2035

nome = input('Qual o seu nome?')

ano_nascimento = int(input(' Qual o seu ano de nascimento?'))

idade_em_2035 = 2035 - ano_nascimento 

print(f'Em 2035 voce vai ter' ,idade_em_2035, 'anos' ,nome,)