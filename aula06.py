#faça um programa que leia a largura e a altura  de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta 
# uma area de 2 metros quadrados

largura = float(input('Digite a largura da parede em metros'))

altura = float(input('Digite a altura da parede em metros'))

area = largura * altura

litros_de_tinta = area / 2

print(f'Voce vai precisar de {litros_de_tinta:.2f} para pintar a parede')