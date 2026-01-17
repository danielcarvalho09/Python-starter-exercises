triangle1 = float(input("Me de um lado do triangulo"))
triangle2 = float(input("Me de outro lado do triangulo"))
triangle3 = float(input("Me de mais um lado do triangulo"))

if triangle1 + triangle2 > triangle3 and triangle2 + triangle3 > triangle1 and triangle1 + triangle3 > triangle2:
    if triangle1 == triangle2 == triangle3:
     print("Esse triangulo é equilatero")
    elif triangle1 == triangle2 or triangle2 == triangle3 or triangle1 == triangle3:
        print("Esse triangulo é isoceles")
    else:
        print("Esse triangulo é escaleno")
else:
    print("Isto não é um triangulo")