'''
        CONVERSOR DE MONEDA LOCAL A dólares V3
'''
def conversor(tipo_pesos, valor_dolar):
    pesos = int(input("¿Cantidad de pesos "+ tipo_pesos+"?: "))
    pesos = float(pesos)
    dolar =  pesos/valor_dolar
    # round se utiliza para indicar cunatos decimales se mostrarán
    dolar =round(dolar,2)
    dolar = str(dolar)
    pesos = str(pesos)
    print("Los $"+ pesos+ " pesos "+tipo_pesos +", son equivalentes a $" + dolar + " dólares americanos.")


menu = """
💰💰💰 BIENVENIDO AL CONVERSOR DE MONEDAS 💰💰💰

1- Pesos Mexicanos 🟢🤍🔴
2- Pesos Argentinos 🇦🇷
3- Pesos Colombianos 🇨🇴

Elige una opción: 
"""

opcion = input(menu)

if opcion == "1":
    # valor del dolar en pesos mexicanos 06052022
    conversor("mexicanos",20.18)

elif opcion =="2":
    # valor del dolar en pesos argentinos 06052022
    conversor("argentinos", 116.30)

elif opcion == "3":
    # valor del dolar en pesos colombianos 06052022
    conversor("colombianos", 4103.53)

else:
    print("INGRESA UN VALOR ENTRE 1 Y 3")