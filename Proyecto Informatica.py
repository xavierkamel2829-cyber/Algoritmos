def calorias_calculo(sexo, peso, altura, edad):
    # Calcula la Tasa Metabólica Basal (Fórmula de Harris-Benedict) multiplicada por el factor de actividad (1.55)
    if sexo == "h": 
        return ((10 * peso) + (6.25 * altura) - (5 * edad) + 5) * 1.55
    else: 
        # Si no es "h", asumimos "m" 
        return ((10 * peso) + (6.25 * altura) - (5 * edad) - 161) * 1.55

def proteina_calculo(peso):
    # Se recomiendan 2.2 gramos de proteína por cada kg de peso corporal
    return peso * 2.2 

def creatina_calculo(peso):
    # Se recomiendan 0.08 gramos de creatina por cada kg de peso corporal
    return peso * 0.08

def calculo_suplementos():
    nombre = input("Ingrese el nombre del usuario: ")
    
    # Bucle para validar que el usuario ingrese únicamente 'h' o 'm'
    while True:
        sexo = input("¿Cual es su genero? (h/m): ").lower()
        if sexo == "h" or sexo == "m":
            break 
        else:
            print("Opción inválida. Por favor, escriba solamente 'h' o 'm'")     
            
    # Bucle con try-except para evitar que el programa falle si ingresan texto en vez de números
    while True:
        try:
            peso = float(input("Ingrese su peso actual (kg): "))
            altura = int(input("Ingrese su altura (cm): "))
            edad = int(input("Ingrese su edad actual: "))
            break 
        except ValueError:
            print("Error: Por favor, ingrese solo valores numéricos válidos.")
            
    # Bucle para validar que seleccionen correctamente una de las 3 opciones del menú
    while True:
        try:
            objetivo = int(input("""Seleccione su objetivo actual: 
1. Volumen (Ganancia de masa muscular)
2. Mantenimiento
3. Definicion (Perdida de grasa corporal):
 """))
            if objetivo in [1, 2, 3]:
                break
            else:
                print("Opción inválida. Seleccione 1, 2 o 3.")
        except ValueError:
            print("Error: Ingrese un número válido (1, 2 o 3).")
            
    # Llamamos a la función para obtener las calorías base
    calorias = calorias_calculo(sexo, peso, altura, edad)
    
    # Ajustamos las calorías totales y el texto del objetivo según la elección
    if objetivo == 1:
        obj_final = "Volumen"
        calorias_consumo = calorias * 1.15
    elif objetivo == 2:
        obj_final = "Mantenimiento"
        calorias_consumo = calorias * 1.0
    elif objetivo == 3:
        obj_final = "Definicion"
        calorias_consumo = calorias * 0.80
        
    # Preguntamos por la creatina 
    while True:
        op_creatina = input("¿Usted desea empezar a consumir creatina? (s/n) ").lower()
        if op_creatina == "s" or op_creatina == "n":
            break 
        else:
            print("Opción inválida. Por favor escriba solamente 's' o 'n'")

    # Resultados
    print("--- PLAN DE SUPLEMENTACIÓN FINAL ---")
    print(f"Usuario: {nombre} | Objetivo: {obj_final}")
    print(f"Calorias quemadas a diario: {calorias:.2f}")
    print(f"Debido a que su objetivo gira en torno a {obj_final}, se recomienda consumir {calorias_consumo:.2f} kcal")
    proteina = proteina_calculo(peso)
    print(f"Proteina: Se recomienda el consumo de {proteina:.2f}g de Proteina para facilitar su meta")
    if op_creatina == "s":
        creatina = creatina_calculo(peso)
        print(f"Creatina: Le recomendamos el consumo de {creatina:.2f}g al día (tomar siempre, incluso días de descanso)")
    else: 
        print("El usuario no implementara creatina en su suplementación")

def main():
    # Bucle que permite evaluar múltiples usuarios o reiniciar el programa
    while True:
        try: 
            print("------PROGRAMA DE SUPLEMENTACION PARA PERSONAS ATLETICAS-----")
            total_usuarios = int(input("Ingrese la cantidad de usuarios que desea evaluar: "))
            if total_usuarios <= 0:
                print("La cantidad debe ser mayor a cero")
                continue
        except ValueError: 
            print("Opcion invalida. Ingrese un numero entero valido")
            continue
            
        # Ciclo for para repetir el proceso según la cantidad de usuarios solicitada
        for i in range(1, total_usuarios + 1):
            print(f"Evaluando usuario {i} de {total_usuarios}")
            calculo_suplementos()
            
        print("Todos los usuarios han sido evaluados con exito")
        continuar = input("¿Desea evaluar otra tanda? s/n: ").lower()
        if continuar != "s":
            break

main()
