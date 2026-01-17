n1 = float(input("Digite um numero"))
n2 = float(input("Digite outro numero"))
n3 = float(input("Digite mais um numero"))

list_num = [n1,n2,n3]

list_decrescente = sorted(list_num, reverse=True)

print(list_decrescente)