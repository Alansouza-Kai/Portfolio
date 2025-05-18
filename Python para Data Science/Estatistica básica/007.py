#Calcule o desvio padrão:
#[12, 15, 14, 10, 18, 20, 22, 17, 19, 16

import statistics

Lista = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16]

desvio_padrao = statistics.stdev(Lista)
print(f"O Desvio Padrão da Lista é: {desvio_padrao:.2f}")
