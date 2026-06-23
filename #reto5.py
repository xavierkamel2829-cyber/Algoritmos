#reto5 
inventario = []
while True :
        opcion = int(input("""Menu de opciones
    1.añadir juego
    2.ver inventario                                    
    3.salir                  
    Cual opcion escoge: """)) 
        if opcion == 1 :
            juego = input ("Cual Juego desea añadir: ")
            inventario.append(juego)
        elif opcion == 2 :
            for i in inventario :
                print(f"- {i}") 
                print("-------------------------------")
        elif opcion == 3 :
         break

        