grade1 = float(input("What was your first grade?"))
grade2 = float(input("What was your second grade?"))

average = grade2 + grade1 / 2

if average >= 10 : 
    print("Aprovado com Distinção")
elif average >= 7  : 
    print("Aprovado")
elif average < 7 : 
    print("Reprovado")
 
