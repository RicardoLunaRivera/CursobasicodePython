'''
CICLO FOR

PROBLEMA: imprimir los números de l 0 al 1000
'''

def main():
    
    '''
    # Solución con WHILE
    contador = 0
    LIMITE = 100
    while contador <= LIMITE:
        print(contador)
        #contador = cotador + 1
        #la linea de 👇 es un atajo para no escribir la linea de☝
        contador += 1
    '''

    # Solución con FOR
    for contador in range(1001):
        print(contador)

if __name__ == '__main__':
    main()

