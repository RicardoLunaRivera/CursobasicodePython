'''
        CONVERSOR DE MONEDA LOCAL A DOLARES V1
'''

pesos = int(input("¿Cantidad de pesos?: "))
pesos = float(pesos)
# valor del dolar en pesos mexicanos 06052022
dolar =  pesos/20.18

# round se utiliza para indicar cunatos decimales se mostrarán
dolar =round(dolar,2)
dolar = str(dolar)
pesos = str(pesos)
print("Los "+ pesos+ " pesos mexicanos, son equivalentes a " + dolar + " dolares americanos")


