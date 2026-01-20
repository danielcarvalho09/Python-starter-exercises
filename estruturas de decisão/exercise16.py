hour_value = float(input("What is the value of your hour?"))
worked_hours = float(input("How many hours do you work this month?"))
brute_wage = hour_value * worked_hours
sindicate = (brute_wage / 100) * 3
fgts = (brute_wage / 100) * 11
inss = (brute_wage / 100) * 10

if brute_wage <= 900:
   ir = 0
elif brute_wage <= 1500:
    ir = (brute_wage / 100) * 5
elif brute_wage <= 2500:
    ir = (brute_wage / 100) * 10
else:
    ir = (brute_wage / 100) * 20
   
liquid_wage = brute_wage - sindicate - inss - ir
print(f"O salário bruto foi de {brute_wage}, o salário liquido foi de {liquid_wage}, o sindicato descontou {sindicate} reais, o inss descontou {inss} o ir descontou {ir} reais e o fgts foi de {fgts} reais")
