# Evaluación de Calificaciones con Rangos: 
# Determina la calificación de un estudiante (A, B, C, D, F) según su puntaje, 
# considerando distintos rangos de puntajes para cada letra. 

A = (4.5, 5.0, 'A')
B = (3.5, 4.49, 'B')
C = (2.96, 3.49, 'C')
D = (2.4, 2.95, 'D')
F = (0, 2.39, 'F')

puntaje = float(input('Ingrese el puntaje del alumno: '))

if(puntaje < 0 or puntaje > 5 ):
    print(f'El puntaje {puntaje} es invalido')
else:
    if(puntaje >= F[0] and puntaje <= F[1]):
        print(f'El alumno ha obtenido una calificacion de {F[2]}')
        
    if(puntaje >= D[0] and puntaje <= D[1]):
        print(f'El alumno ha obtenido una calificacion de {D[2]}')
        
    if(puntaje >= C[0] and puntaje <= C[1]):
        print(f'El alumno ha obtenido una calificacion de {C[2]}')

    if(puntaje >= B[0] and puntaje <= B[1]):
        print(f'El alumno ha obtenido una calificacion de {B[2]}')

    if(puntaje >= A[0] and puntaje <= A[1]):
        print(f'El alumno ha obtenido una calificacion de {A[2]}')