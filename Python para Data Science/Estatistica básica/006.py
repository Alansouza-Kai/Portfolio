#Calcule a média aritimética simples, moda, mediana das seguintes notas.
#5.7, 6.5, 6.9, 8.3, 8, 4.2, 6.3, 7.4, 6.9

import statistics

Lista = [5.7, 6.5, 6.9, 8.3, 8, 4.2, 6.3, 7.4, 6.9]

print(f'média: {statistics.mean(Lista)},'
      f'\nmoda: {statistics.mode(Lista)}'
      f'\nmediana: {statistics.median(Lista)}')

