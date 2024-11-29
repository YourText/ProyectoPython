rep = 5
contador = 0
while contador < rep:
    mensaje = f"{contador} Segundo"
    if contador > 1:
        mensaje = f"{contador} Segundos"
    print(mensaje)
    contador += 1