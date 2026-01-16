wage_hour = int(input("How much you earn per hour?"))
hour_work = int(input("How many hours do you work this month?"))

wage_brute =  wage_hour * hour_work
ir = (wage_brute / 100) * 11
inss = (wage_brute / 100) * 8
sindicato = (wage_brute / 100) * 5

descounts = ir + inss + sindicato
liquid_wage = wage_brute - descounts

print(f"The bruta wage is {wage_brute}, you paid {ir} in ir,{inss} in inss and {sindicato} in sidicato, you liquid wage is {liquid_wage} ")