from random import randint
loteria = [""]*6
i = 0
while i < len(loteria):
    num = randint(1,60)
    repetiu = "n"
    k = 0
    while k < i:
        if num == loteria[k]:
            i -= 1
            repetiu = "s"
            break
        k += 1
    if repetiu == "n":
        loteria[i] = num
    i += 1
print(loteria)


numeros = []

while len(numeros) < 6:
    num = randint(1,60)
    if num not in numeros:
        numeros.append(num)
print(numeros)
