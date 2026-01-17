name = str(input("Digite uma letra"))
if len(name) > 1:
 print("digite somente uma letra")
else: 
    if name == "F":
     print("Feminino")
    elif name == "M":
     print("Masculino")
    else: 
        print("Sexo inválido")