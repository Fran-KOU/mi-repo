decimal = int(input("Ingrese un valor positivo de dos cifras a transformar a binario: "))
decimal1= decimal
binario1 = 0
binario2 = 0
binario3 = 0
binario4 = 0
binario5 = 0
binario6 = 0
binario7 = 0

while decimal > 99 or decimal < 0:

    print("Ingrese un valor valido.")
    decimal = int(input("Ingrese un valor positivo de dos cifras a transformar a binario: "))
    decimal1 = decimal

if decimal1 >= 64:
    decimal1 = decimal1 - 64
    binario1 = 1

if decimal1 >= 32:
    decimal1 = decimal1 - 32
    binario2 = 1

if decimal1 >= 16:
    decimal1 = decimal1 - 16
    binario3 = 1

if decimal1 >= 8:
    decimal1 = decimal1 - 8
    binario4 = 1

if decimal1 >= 4:
    decimal1 = decimal1 - 4
    binario5 = 1

if decimal1 >= 2:
    decimal1 = decimal1 - 2
    binario6 = 1

if decimal1 >= 1:
    decimal1 = decimal1 - 1
    binario7 = 1

print(f"La conversion de {decimal} a binario da un resultado de: {binario1}{binario2}{binario3}{binario4}{binario5}{binario6}{binario7}")
