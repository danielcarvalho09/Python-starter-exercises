import math
tamanho_parede = int(input("Qual é o tamanho em metros quadrados da área que será pintada"))
litros_utilizados = math.ceil(tamanho_parede / 6)
lata18l = math.ceil(litros_utilizados / 18)
latal3l = math.ceil(litros_utilizados / 3.6)
lata18l_semarredondar = litros_utilizados / 18
sobra_or_not = litros_utilizados % 18
if sobra_or_not != 0:
 folga = (sobra_or_not / 100) * 10
 lata3l_total = folga + sobra_or_not
 lata3l_mistura = math.ceil(lata3l_total/ 3.6)

print(f"Para o menor desperdício possível, misture {lata3l_mistura} de latas de 3,6L e {lata18l} de latas de 18L")