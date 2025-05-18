#Calcule o primeiro e o terceiro quartis:
#[12, 15, 14, 10, 18, 20, 22, 17, 19, 16, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

Lista = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

import numpy as np

print(f'{np.percentile(Lista, 25)}')
print(f'{np.percentile(Lista, 75)}')
