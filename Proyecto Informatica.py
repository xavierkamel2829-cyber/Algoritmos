#Programa para mejorar la eficiencia en el desempeño deportivo
def calorias() :
    edad=int(input("cuanto años teneis (años): "))
    peso=int(input("Cuanto pesais (Kg): "))
    genero=input("soy mujel 'm' , homble 'h' ").lower
    estatura=int(input("cuando medies (en Cm) "))
    if genero=='h':
        consumo_h=(10*peso)+(6.25*estatura)-((5*edad)+5)*1.2
        print("tu consumo de calorias medio seria: ", consumo_h)
    else: 
        consumo_m=(10*peso)+(6.25*estatura)-((5*edad)-161)*1.55
        print("tu consumo de calorias medio seria: ", consumo_m)
calorias()
