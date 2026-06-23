import random
def Opcion_pc() :
    opciones = [1, 2 , 3]
    return random.choice(opciones)
def opcion_usuario(opcion_us , computadora) :
    if opcion_us == computadora :
        return (f"La pc escogió: {computadora} , han empatado")
    elif (opcion_us== 1 and computadora == 3) or (opcion_us== 2 and computadora == 1) or (opcion_us== 3 and computadora == 2) :  
        return(f"La pc escogió: {computadora} , has ganado")
    else :
        return (f"La pc escogió: {computadora} , has perdido...")
def main()  :
    while True :
        opcion_us = int(input("""Menu de opciones
        1 piedra
        2 papel
        3 tijera
        4 salir                      
        escoja una opcion: """))
        computadora= Opcion_pc()
        if opcion_us == 4 :
            break
        elif opcion_us in [1, 2, 3]: 
             print (opcion_usuario(opcion_us , computadora))
             Reinicio = input("desea volver a jugar (s/n): ").lower()
             if Reinicio == "n" :
                break
        else :
            print ("Seleccione una opcion valida: ")
            continue    
main() 
