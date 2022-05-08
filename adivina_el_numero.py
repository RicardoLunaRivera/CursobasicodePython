import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_adivinado = int(input('Adivina el número que está entre el 1 y el 100: '))

    while numero_adivinado != numero_aleatorio:
        if numero_adivinado < numero_aleatorio:
            print('Escoge un número más grande')
        else:
            print('Elige un número más pequeño')
        numero_adivinado = int(input('Escribe otro número: '))
    print('¡Ganaste!')

if __name__ == '__main__':
    run()