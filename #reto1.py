#reto1
print ("programa para saber si una persona se puede montar en la atraccion")
edad = int(input("¿cual es tu edad?: "))
estatura = float(input("¿cual es tu estatura en centimetros?: "))
if edad < 13 and estatura < 141 :
    print ("lo lamento no cumples los requisitos")
else :
     print("excelente, puedes pasar")