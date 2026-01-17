turn = str(input("Em qual turno você estuda?M - Matutino\nV - Vespertino\nN - Noturno."))

if len(turn) > 1 :
    print("digite somente uma letra")
elif turn == "M":
    print("Bom dia!")
elif turn == 'V':
    print("Boa tarde!")
else:
    print("Boa noite!")