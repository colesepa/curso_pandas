""" 
Construir uma loteria da babilonia:

1 - Programa escolhe um numero randomico de 1 a 15;
2 - Usuario terá 3 chenaces;
3 - Mostrar feedback das alternativas (chute é maior ou menor que o valor);
4 - Parabenizar o susuario em caso de acerto:
"""

#%%
import random

# dir(Random)

choice = random.randint(1,15)
# print(choice)
c = 0
while c < 3:
    tip =  int(input('Digite um núemero de 1 à 15:  '))
    
    if tip == choice:
        print('Parabéns! Você acertou')
        break
    
    elif tip > choice:
        print('Valor errado, seu valor é maior do que o número surpresa!')
        
    else:
        print('Valor errado, seu valor é menor do que o número surpresa!')
    c += 1
     

""" 
O for também tem uma condiconante else que roda após o termino do for, caso o loop
rode sem um break interno 

"""

# %%

import random

random_choice = random.randint(1, 15)

i = 1

while i <= 3:
    tip = int(input('Digite um número: '))
    if tip in range (1,16):
        
        if tip == random_choice:
            print('Parabéns! Você acertou')
            break
        
        elif tip > random_choice:
            print('Valor errado, seu valor é maior do que o número surpresa!')
        
        else:
            print('Valor errado, seu valor é menor do que o número surpresa!')
            
        print(f'Você só tem mais {3 - i} chances.')
        
        i +=1
    else:
        print('Valor inválido, escolha somente entre 1 e 15!')
        


""" Refazer com o try e except """
# %%
