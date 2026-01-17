n1 = float(input("Digite um numero"))
n2 = float(input("Digite outro numero"))
n3 = float(input("Digite mais um numero"))

if n1 > n2 and n1 > n3 :
    print(f"o maior é o {n1}")
    if n2 < n3:
        print(f"O menor é o {n2}")
    else:
        print(f"O menor é o {n3}")
elif n2 > n1 and n2 > n3:
    print(f"o maior é o {n2}")
    if n1 < n3:
        print(f"O menor é o {n1}")
    else:
        print(f"O menor é o {n3}")
else: 
 print(f"o maior é o {n3}")
 if n1 < n2:
        print(f"O menor é o {n1}")
 else:
        print(f"O menor é o {n2}")