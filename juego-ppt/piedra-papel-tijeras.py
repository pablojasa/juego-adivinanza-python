# jugador1 = input("Hola Jugador 1! ¿Que eliges? ¿Piedra, papel o tijeras?: ")
# jugador2 = input("Hola Jugador 2! ¿Que eliges? ¿Piedra, papel o tijeras?: ")

# if jugador1 == jugador2: 
#     print("¡Ha sido un empate!")
# elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
#     print("Ha ganado el Jugador 1")
# else:
#     print("Ha ganado el Jugador 2")


nombre1 = input("¿Como se llamará el Jugador 1?: ")
nombre2 = input("¿Como se llamará el Jugador 2?: ")



jugador1 = input(f"Hola {nombre1}! ¿Que eliges? ¿Piedra, papel o tijeras?: ").strip().lower()
jugador2 = input(f"Hola {nombre2}! ¿Que eliges? ¿Piedra, papel o tijeras?: ").strip().lower()

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"


if jugador1 == jugador2: 
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print(f"Ha ganado {nombre1}!🏆")
else:
    print(f"Ha ganado {nombre2}!🏆")