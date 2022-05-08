def main():
    # uso de CONTINUE
    #el programa solo imprimira los números multiplos de 2
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    
    #Uso de BREAK
    #el program se detendrá hasta llegar al número indicado
    # for i in range(100):
    #     print(i)
    #     if i ==89:
    #         break


    texto = input("Escribe una frase: ")
    for letra in texto:
        if letra == 'a':
            break
        print(letra)

if __name__ == '__main__':
    main()