weight_fish = float(input("Qual é o peso do seu peixe?"))
if weight_fish > 50 :
 excedent = weight_fish - 50
 multa = excedent * 4
 print(f"O valor que deverá ser pago é {multa} reais e o excesso foi de {excedent} kg")
else :
 print("Não precisa pagar multa")