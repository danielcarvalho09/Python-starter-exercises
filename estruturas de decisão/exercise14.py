wage = int(input("What is your wage"))

if wage > 1500:
    perc = 5
    wage_readjustment = (wage / 100) * perc
    wage_after = wage + wage_readjustment
elif wage < 1500 and wage > 700 :
    perc = 10
    wage_readjustment = (wage / 100) * perc
    wage_after = wage + wage_readjustment
elif wage < 700 and wage > 280 :
    perc = 15
    wage_readjustment = (wage / 100) * perc
    wage_after = wage + wage_readjustment
else: 
    perc = 10
    wage_readjustment = (wage / 100) * perc
    wage_after = wage + wage_readjustment
    
print(f"Seu salário antes: {wage}.O percentual do aumento foi de {perc} o valor do aumento foi {wage_readjustment} e seu novo salário é{wage_after}")
    
    