print ("Programa para calcular si una sección aprobó una materia y conocer su promedio tanto individual como grupal.")
while True :
    total_estudiantes = int(input( "¿Cuantos alumnos hay en la sección que se va a evaluar?: "))
    if total_estudiantes <= 0 :
       print("La cantidad minima de estudiantes es de 1.")
       continue
    contador = 0
    for i in range (total_estudiantes) :
        nombre_alumno= (input("Coloque el nombre del estudiante a evaluar: ")) 
        nota1= int(input("Coloque la primera nota de " + nombre_alumno + ": "))
        nota2= int(input("Coloque la segunda nota de " + nombre_alumno + ": "))
        nota3= int(input("Coloque la tercera nota de " + nombre_alumno + ": "))
        nota4= int(input("Coloque la cuarta nota de " + nombre_alumno + ": "))
        nota5= int(input("Coloque la quinta nota de " + nombre_alumno + ": "))
        suma_de_notas= nota1 + nota2 + nota3 + nota4 + nota5 
        promedio_individual= suma_de_notas / 5
        contador = promedio_individual + contador
        if suma_de_notas >= 60 : 
            print(nombre_alumno + " pasó satisfactoriamente la materia, con una nota promedio de " , promedio_individual )  
        else :
            print (nombre_alumno + " no aprobó la materia, ya que cuenta con una nota promedio de " , promedio_individual) 
    promedio_de_la_seccion = contador / total_estudiantes
    print("el promedio de la seccion fue" , promedio_de_la_seccion )
    opcion = input("desea hacerlo con otra sección? (s/n): ") 
    if opcion == "n" : 
     break



    
    

    
    
    
    
    
    

    
    
    
    
    
  