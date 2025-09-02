""" 
Estudos dos métodos e funções built-in do python.

"""

#%%

#abs() -> função de retorno de um valor absoluto -34 -> 34

a = abs(-34)
print(a) # -> 34


"""
Podemos utilizar os métodos internos object.__abs__() de um int/float e ter o mesmo 
retorno. Os "dunder methods" são métodos internos de um objeto.
"""

#%%

# x = -34
# x.__abs__() -> 34

x = -34
print(x.__abs__()) # -> 34 

#%%

#all(<iterable>) -> Retorna True se dentro do iteravel todos os valores são não falso (False, Vazio, 0...)

elements = [['casa', 'roupa','comida'],"abc"] #-> Lista/Dicionario/Sets/Strings são iter.
elements2 = []
elements3 = 35

print(all(elements)) #-> True
print(all(elements2)) #-> False
#print(all(elements3)) -> Typerror

#Essa função serve para verificar se um conjuntos de resultados são todos verdadeiros.

resultados = [
    1 < 2,
    "a" in "abc",
    True
]

print(all(resultados)) #-> True

resultados = [
    1 > 2,
    "a" not in "abc",
    False
]

#Para verificar se todos são falsos adicionamos o not na frente!
print(not all(resultados)) #-> True

# A função all pode ser equivalente a:

#%%
def _all(_iter) -> bool:
    for i in _iter:
        try:
            for x in i:
                pass
        except:
            return False
    return True

elements = [['casa', 'roupa','comida'],"abc",3]

_all(elements)
#%%

"""
No mesmo sentido da função all() o any() apresenta a verificação se ao menos um valor dentro do iteravel, sendo o iteravel vazio 
retorna Falso. 
"""
elements = [['casa', 'roupa','comida'],"abc",3]
elements2 = [False, 0]

print(any(elements)) #-> True
any(elements2) #-> False

# %%

""" 
A função ascii() "Strigzeriza" qualquer retorno de uma função. Como se ela escrevesse um log em formato de texto e escapando
caracteres unicode (acentos, ç...)
"""


print(type(str)) #-> <class 'str'> isso é uma informaçao do tipo
print(ascii(str)) #-> "<class 'str'>" isso é uma string
repr(str)

#Tudo que temos no python é uma classe estanciada da classe type!

# %%
""" 
Classe bool() retorna False se for passada com obeject vazio, e True se tiver alguma coisa.
"""

print(bool('matheus')) #-> True
print(bool() )#-> False
print(bool(0)) #-> False

#%%

""" 
O  Commando hash() é usado para gerar valores únicos de identificaçao, na instancia que ele está rodando. O comando é usado para definir as identificações 
de elementos como as chaves de um dicionário. Com essa inforamção, fica mais claro o porque da aleatoreidade das ordens de um dicionário, e da velocidade de busca 
dentro de um dicionário.
"""

senha = '@Princesa1307'
tentativa1 = '@princesa1307'
tentativa2 = '@Princesa1307'
print(hash(senha))
print(hash(tentativa1))
print(hash(tentativa2))

print(senha == tentativa1) # -> Falso
print(senha == tentativa2) # -> True

""" 
Para o uso de hashs com objetivos de segfunraça nmo Python, recomenda-se o uso da biblioteca ~ hashlib ~
"""
# %%

""" 
Função enumerate(iterabel, start=0) -> Tupla (index, valor): Função que retorna uma tupla de valores, 
indicando o index desse valor, dentro iteravel e retorna o proprio valor.
O elemento iterable deve ter o dunder method __next__(). 
"""

elements = ['casa', 'roupa','comida',"abc"] 

a = list(enumerate(elements))

print(a) #-> [(0, 'casa´), (1, 'roupa'), (2, 'comida'), (3, "abc")]
   

# %%

"""
O comando filter(fucrion, iterable) -> iterable; A função filtra valores TRUE da vberificaçao passada 
no parâmetro <function>
"""

elements = [3, 5, 7, 2, 8, 1]

filtered_elements = filter(lambda x: x  > 2, elements)

print(list(filtered_elements)) #-> [3,4,7,8]

""" 
itertools.filterfalse(): Função que retorna os valores negativos da expressão passada.

"""


# %%

"""
hasattr(object, name) -> Verifica a existência de um atributo em uma determinada classe.
"""

# %%

a = "Matheus"

id(a)

# %%
import sys

float_info = sys.float_info


float_info.epsilon
float_info.dig
# sys.executable
# %%

import sys
sys.get_int_max_str_digits()
sys.getrecursionlimit()
sys._getframe()
sys.hash_info
sys.implementation
sys.is_finalizing()
sys.path
sys.path_hooks
sys.platform
sys.platlibdir
sys.prefix
sys.stdin
sys.thread_info
sys.version
#%%
import os

os.name


# %%
