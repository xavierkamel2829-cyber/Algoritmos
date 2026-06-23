Algoritmo Piedra_Papel_o_Tijera
	Definir opcion_pc , opcion_us Como Entero
	Dimension opciones[3]
	opcion_pc<-Aleatorio(1,3)
	opciones[1]<-"Piedra"
	opciones[2]<-"Papel"
	opciones[3]<-"Tijera"
	Escribir "Juego de piedra papel o tijera"
	Escribir "Aqui tienes las opcines"
	Escribir "1.Piedra"
	Escribir "2.Papel"
	Escribir "3.Tijera"
	Escribir "Elige una"
	Leer opcion_us
	Si opcion_us<>1  y opcion_us<>2 y opcion_us<>3 Entonces
		Escribir "Opcion invalida"
	SiNo
		Escribir "La PC ESCOGIO: " opcion_pc " Y TU ELEGISTE: " opcion_us
		
		Si opcion_us=opcion_pc Entonces
			Escribir "Empate!!"
		SiNo
			si opcion_us=1 y opcion_pc=3 o opcion_us=2 y opcion_pc=1 o opcion_us=3 y opcion_pc=2 Entonces
				Escribir "GANASTE!!"
			SiNo
				Escribir "Perdiste Fracasado..."
			FinSi
		FinSi
	FinSi
FinAlgoritmo
