import random

print("-" * 73)
print("|   Bienvenido al Juego de Piedra, Papel o Tijera espero te diviertas   |")
print("-" * 73)

opcion = ("piedra", "papel", "tijera")
jugador_gano = 0
pc_gano = 0
round = 1

while True:
    print(f'*' * 10)
    print(f'Ronda {round}')
    print('*' * 10)
    print(f"\nPuntos Pc: {pc_gano}")
    print(f"Puntos Jugador: {jugador_gano}")

    jugador = input("Escoge: Piedra, Papel o Tijera -> ")
    print("-" * 100)
    jugador = jugador.lower()

    if not jugador in opcion:
        print(f"Esa opcion no es valida elije alguna de estas -> {opcion}")
        continue

    pc = random.choice(opcion)
    print(f"Jugador escogio: {jugador}")
    print(f"Pc escogio: {pc}")
    print("-" * 100)


    if jugador == pc:
        print("Resultado: Empate!")
    elif (
        jugador == "piedra" and pc == "tijera" 
        or jugador == "papel" and pc == "piedra" 
        or jugador == "tijera" and pc == "papel"
    ):
        print(f"{jugador} le gana a {pc}")
        print("Resultado: Jugador a ganado")
        jugador_gano += 1
    else:
        print(f"{pc} le gana a {jugador}") 
        print("Resultado: Pc gano")
        pc_gano += 1

    round += 1

    print("-" * 100)

    if pc_gano == 3 or jugador_gano == 3:
        if pc_gano == 3:
            print('El rotundo ganador es la computadora')
            print('Lo siento Intentalo de nuevo')
        else:
            print('El rotundo ganador es el Jugador')
            print('En hora buena eres un ganador')

        print(f"\nMarcador final - Jugador: {jugador_gano}, PC {pc_gano}")
        respuesta = input("\n¿Deseas jugar otra vez?(s/n): ").strip().lower()
        if respuesta == "s":
            jugador_gano = 0
            pc_gano = 0
            round = 1
            continue
        else:
            print("Hasta luego 👋🏽")
            break