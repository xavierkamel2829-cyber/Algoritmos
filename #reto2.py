#reto2 
print ("programa para contar una x cantidad de productos en un supermercado")
total_de_productos = 0
while True :
    producto = (input("""Lista de productos
1. pan
2. leche
3. huevo   
Escriba el producto que desea añadir al carrito: """)).lower()
    if producto in ["pan" , "leche" , "huevo"] :
        total_de_productos = total_de_productos + 1
        print("se ha añadido un producto")
        respuesta = input("desea añadir otro producto o desea pagar los productos actuales (añadir/pagar)?: ").lower()
        if respuesta == "añadir" :
            continue
        else :
            print(f"la cantidad de productos a pagar es: {total_de_productos}")
            break
    else :
        print("escriba un producto valido")
        continue

