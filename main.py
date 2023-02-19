from calculadora import Calculadora
from comodo import  Comodo

calc = Calculadora()

cmd = Comodo(
    input('Qual a largura do cômodo?'),
    input('Qual a profundidade do cômodo?')
)


print(
    'A área das paredes é: ',
    calc.calcular_area_paredes(cmd)
)

print(
    'A área do teto é de: ',
    calc.calcular_area_teto(cmd)
)

print(
    'A litragem de tinta necessária é de: ',
    calc.calcular_litragem_tinta(), ' litros.'
)

