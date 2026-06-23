#reto3

def proceso_de_adminsion(promedio , materiasR ) :
    if promedio >= 90 and materiasR == 0 :
        return("perfecto, tienes una beca del 100%")
    elif promedio >= 80 and materiasR == 0 :
        return("felicidades, tienes una beca del 50%")
    else :
        return("lo sentimos no quedaste para ninguna beca")
    
def main() :   
    while True : 
        promedio = float(input("coloque su promedio de notas: "))
        materiasR = int(input("coloque el numero de materias reprobadas: "))
        print (proceso_de_adminsion(promedio , materiasR ))
        respuesta = input("desea volver a pasar?:" )
        if respuesta == "n" :
            break
        else :
            continue
    
main()
