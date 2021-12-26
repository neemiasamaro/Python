altura = float(input("Entre com sua altura: "))
tipo = str(input("Entre com seu sexo: "))

if(tipo == 'h'):
   peso = str((72.7 * altura) - 58)
   print("Seu peso ideal seria de " + peso + " kg")
elif(tipo == 'm'):
    peso = str((62.1 * altura) - 44.7)
    print("Seu peso ideal seria de " + peso + " kg")
else:
    print("Erro")