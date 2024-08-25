# Escribir un programa que muestre los números del 2000 al 0, pero de 250 en 250.

for i in range(2000, -1, -250):
    match i:
        case 2000:
            print(i)
        case 1750:
            print(i)
        case 1500:
            print(i)
        case 1250:
            print(i)
        case 1000:
            print(i)
        case 750:
            print(i)
        case 500:
            print(i)
        case 250:
            print(i)
        case 0:
            print(i)