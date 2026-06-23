import random
def opciones_juego():
    opciones = [1,2,3] #1. Piedra, 2. Papel, 3. Tijeras
    return random.choice(opciones)
def proceso_de_juego(usuario, pc):
    if usuario == pc:
        return "Es un empate!"
    if (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
        return "Ganaste!"
    else:
        return "Perdiste... Suerte la proxima:)"
def main():
    print("Juego de piedra papel o tijeras")
    print("""1. Piedra
2. Papel
3. Tijeras
4. Salir""")
    while True:
        usuario = int(input("Seleccine una opcion... "))
        if usuario == 4:
            break
        if usuario not in [1,2,3]:
            print("Seleccione una opcion valida")
        computadora = opciones_juego()
        resultado = proceso_de_juego(usuario, computadora)
        print(f"{resultado}, la opcion de la pc fue: {computadora}")
main()