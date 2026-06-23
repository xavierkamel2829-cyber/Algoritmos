while True :
    print ("programa para calcular si un grupo de alumnos pasa o no pasa")
    est1= str(input("coloque el nombre del primer estudiante: "))
    not1= int(input("coloque la primera nota de " + est1 + ": "))
    not2= int(input("coloque la segunda nota de " + est1 + ": "))
    not3= int(input("coloque la tercera nota de " + est1 + ": "))
    not4= int(input("coloque la cuarta nota de " + est1 + ": "))
    not5= int(input("coloque la quinta nota de " + est1 + ": "))
    max1= not1 + not2 + not3 + not4 + not5
    pro1= max1/5 
    if not1 + not2 + not3 + not4 + not5 >= 60: 
        print(est1 + " paso satisfactoriamente, con un promedio de " , pro1 )
   
    elif  not1 + not2 + not3 + not4 + not5 < 60: 
        print (est1 + "raspó con un promedio de " , pro1)
    opcion = input("desea hacerlo con otro alumno? (s/n): ") 
    if opcion == "n" : 
        break