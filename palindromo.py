import re


def palindromo(palabra):
    #La palabra debe estr en minúsculas
    palabra = palabra.lower()
    #La palabra no debe tener espacios
    palabra = palabra.replace(' ', '')
    #la palabra se debe poder leer al revez
    palabra_invertida = palabra[::-1]
    #palabra = palabra.lower().replace(' ','')
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo =palindromo(palabra)
    if es_palindromo == True:
        print("Es un palíndromo.")
    else:
        print("No es palíndromo.")    

#Entry point
if __name__ == '__main__':
    main()
