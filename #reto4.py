#reto4
aprobados = 0
reprobados = 0
for nota in [55, 85, 40, 90, 70, 65] :
    if nota >= 60 :
        aprobados = aprobados + 1
    else :
        reprobados = reprobados + 1

print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos reprobados: {reprobados}")