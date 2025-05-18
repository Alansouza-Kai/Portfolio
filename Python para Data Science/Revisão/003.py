'''Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
V = (4/3) . π . r³
A = 4 . π . r²
Saída esperada:
Volume da Esfera: Y
Área da esfera: X'''


Raio = float(input("Digite o valor do raio: "))

V = (4/3) * 3.1415 * (Raio**3)
A = 4 * 3.1415 * (Raio**2)

print(f'Volume da Esfera: {V}\n'
      f'Área da esfera: {A}')