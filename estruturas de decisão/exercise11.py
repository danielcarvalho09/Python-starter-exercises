p1 = float(input("Preço primeiro produto:"))
p2 = float(input("Preço segundo produto:"))
p3 = float(input("Preço terceiro produto:"))

if p1 < p2 and p1 < p3:
    print(f"compre o produto com preço de {p1} reais")
elif p2 < p1 and p2 < p3:
    print(f"compre o produto com preço de {p2} reais")
else: 
    print(f"compre o produto com preço de {p3} reais")