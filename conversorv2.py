'''
        CONVERSOR DE MONEDA LOCAL A d贸lares V2
'''

menu = """
馃挵馃挵馃挵 BIENVENIDO AL CONVERSOR DE MONEDAS 馃挵馃挵馃挵

1- Pesos Mexicanos 馃煝馃馃敶
2- Pesos Argentinos 馃嚘馃嚪
3- Pesos Colombianos 馃嚚馃嚧

Elige una opci贸n: 
"""

opcion = input(menu)

if opcion == "1":
    pesos = int(input("驴Cantidad de pesos Mexicanos?: "))
    pesos = float(pesos)
    # valor del dolar en pesos mexicanos 06052022
    dolar =  pesos/20.18
    # round se utiliza para indicar cunatos decimales se mostrar谩n
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Mexicanos, son equivalentes a $" + dolar + " d贸lares americanos")

elif opcion =="2":
    pesos = int(input("驴Cantidad de pesos Argentinos?: "))
    pesos = float(pesos)
    # valor del dolar en pesos argentinos 06052022
    dolar =  pesos/116.30
    # round se utiliza para indicar cunatos decimales se mostrar谩n
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Argentinos son equivalentes a $" + dolar + " d贸lares americanos")

elif opcion == "3":
    pesos = int(input("驴Cantidad de pesos Colombianos? : "))
    pesos = float(pesos)
    # valor del dolar en pesos colombianos 06052022
    dolar =  pesos/4103.53
    # round se utiliza para indicar cunatos decimales se mostrar谩n
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Colombianos, son equivalentes a $" + dolar + " d贸lares americanos")

else:
    print("INGRESA UN VALOR ENTRE 1 Y 3")

