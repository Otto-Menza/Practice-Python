#Break and Continue
for numero in range(1, 10):
    if numero % 2 == 0: #numeor impar
        print(numero)
        break #Salimos del ciclo a penas el primer if
print('palabra Continue')
for numero in range(1,10):
    if numero % 2 == 1:
        continue
        print('Esto no sale, por el continue')
    print(numero)