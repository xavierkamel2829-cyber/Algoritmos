//BUZZ y SISS con limite por el usuario y mostrar 5 y 2 
Algoritmo BUZZ_SiSS
	Escribir "Defina el numero inicial de su rango"
	leer num1
	Escribir "Defina su numero final"
	leer num2
	Escribir "cual multiplo desea sustituir por SISS?"
	Leer multi1
	Escribir "cual multiplo desea sustituir por BUZZ?"
	Leer multi2
	Para i<-num1 Hasta num2 Con Paso 1 Hacer
		Si (i%multi1=0) y (i%multi2=0) Entonces
			Escribir"SissBuzz"
		SiNo
			si i%multi1=0 Entonces
				Escribir"SISS"
			SiNo
				si i%multi2=0 Entonces
					Escribir "Buzz"
				SiNo
					Escribir i
				FinSi
			FinSi
		FinSi
	Fin Para
	
FinAlgoritmo
