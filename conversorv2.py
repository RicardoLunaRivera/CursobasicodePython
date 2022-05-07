'''
        CONVERSOR DE MONEDA LOCAL A dólares V2
'''

menu = """
💰💰💰 BIENVENIDO AL CONVERSOR DE MONEDAS 💰💰💰

1- Pesos Mexicanos 🟢🤍🔴
2- Pesos Argentinos 🇦🇷
3- Pesos Colombianos 🇨🇴

Elige una opción: 
"""

opcion = input(menu)

if opcion == "1":
    pesos = int(input("¿Cantidad de pesos Mexicanos?: "))
    pesos = float(pesos)
    # valor del dolar en pesos mexicanos 06052022
    dolar =  pesos/20.18
    # round se utiliza para indicar cunatos decimales se mostrarán
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Mexicanos, son equivalentes a $" + dolar + " dólares americanos")

elif opcion =="2":
    pesos = int(input("¿Cantidad de pesos Argentinos?: "))
    pesos = float(pesos)
    # valor del dolar en pesos argentinos 06052022
    dolar =  pesos/116.30
    # round se utiliza para indicar cunatos decimales se mostrarán
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Argentinos son equivalentes a $" + dolar + " dólares americanos")

elif opcion == "3":
    pesos = int(input("¿Cantidad de pesos Colombianos? : "))
    pesos = float(pesos)
    # valor del dolar en pesos colombianos 06052022
    dolar =  pesos/4103.53
    # round se utiliza para indicar cunatos decimales se mostrarán
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos Colombianos, son equivalentes a $" + dolar + " dólares americanos")

else:
    print("INGRESA UN VALOR ENTRE 1 Y 3")

