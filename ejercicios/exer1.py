#En la "Franco Champions League",cada equipo registra la cantidad de goles que han anotado 
# sus jugadores en la temporada. El entrenador quiere identificar al máximo goleador de su equipo,
# es decir, el jugador con la mayor cantidad de goles.
# Sin embargo, si dos o más jugadores tienen la misma cantidad máxima de goles, 
# el entrenador solo considerará al primero que apareció en la lista.

num_jugadores = int(input("Ingresa la cantidad de jugadores en el equipo: "))

if num_jugadores > 0:
    x = -1
    goles = []

    for i in range (num_jugadores):
        gol = int(input(f"Ingresé la cantidad de goles del jugador {i+1}: "))
        goles.append(gol)
        
    if x<gol:
            x = gol
            max_jugador = i +1
            
    print("""
            El maximo goleador metio %i goles

            """ %(x))
else:
    print("No hay jugadores")