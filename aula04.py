#Escreva um programa que leia tres notas de um aluno e retorne a media dele

print(f'Ola estudante, confira sua media do periodo letivo!')  

nome = input(f'Digite seu nome:')

nota_1 =  float(input(f' Digite a sua primeira nota:'))

nota_2 = float(input(f'Digite sua segunda nota:'))

nota_3 = float(input('Digite sua terceira nota:'))

faltas = int(input(f'Quantas faltas voçe teve nesse semestre?'))

media = (nota_1 + nota_2 + nota_3) /3



print(f'{nome} sua media foi {media:.2f}')

if media >= 7 and faltas <9:
    print(f'Voçe foi aprovado {nome} Parabéns')
    input(f'Digite seu e-mail para enviarmos seu certificado:')
    print(f'email enviado com sucesso!')    
    
else:
    print('Voce foi reprovado pelo numero de faltas ou pela media nao atingida')    

