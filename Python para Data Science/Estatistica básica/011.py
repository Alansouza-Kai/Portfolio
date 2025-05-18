#Identifique a Assimetria:
#X = 3, 3, 4, 4, 5, 6, 7, 9, 12, 20

import statistics
X = 3, 3, 4, 4, 5, 6, 7, 9, 12, 20

média = statistics.mean(X)
moda = statistics.mode(X)
mediana = statistics.median(X)
desvio_padrao = statistics.stdev(X)

Assimetria = (média - moda)/ desvio_padrao

if Assimetria == 0:
    print("A Distribuição é simétrica")
elif Assimetria > 0:
    print("A Cauda da direta é a mais longa (Assimetria positiva)")
else:
    print("A cauda da esquerda é a mais longa (assimetria negativa)")