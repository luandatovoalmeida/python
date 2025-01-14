# recaptulando clone e pull do github para git

print (f'Vamos começar a fazer seu cadastro.')

nome = input(f'Digite seu nome:')

idade = int(input(f'Digite sua idade:'))

email = input(f'Digite seu e-mail:')

cliente = (f"print nome: {nome},  idade: {idade}, email: {email} ")

print(f'Confira se seus dados estão corretos')

print (f"\n{nome} \n {idade} \n {email}")

dados_corretos = input('Estão corretos? (sim ou não): ')

if dados_corretos.lower() == 'sim':
    print('Cadastro realizado com sucesso!')
else:
    print('Vamos tentar novamente.')






   
 

