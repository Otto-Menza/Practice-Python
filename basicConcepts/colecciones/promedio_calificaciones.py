# promedio de calificaicones:
cantidad_notas = int(input('Ingresa cantidad de calificaciones: '))
acumulado = 0
calificaciones = []
for nota in range(cantidad_notas):
    nota = float(input(f'Calificación [{nota+1}]: '))
    acumulado += nota
    calificaciones.append(nota)
promedio = acumulado/cantidad_notas
print(f'Las calificaciones son:{calificaciones}')
print(f'El primedio fue de: {promedio}')