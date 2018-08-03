# def tabuada():
#     print("==== Tabuada ====")
#
#     numero = int(input("Digite um número para saber sua tabuada: "))
#
#     s = 1
#
#     while s <= 10:
#         print("{} x {} = {}" .format(numero, s, numero*s))
#         s = s + 1
#
# tabuada()


#Exemplo de função com parâmetro e sem retorno
#
# def exemplo2(num):
#
#     print("O número informado é: {}" .format(num))
#
#     if(num %2 == 0):
#         print("Este número é par !")
#     else:
#         print("Número ímpar detectado !")
#
# exemplo2(10)
#
# b = int(input("Digite um número: "))
# exemplo2(b)

#Exemplo de função com parâmetro e com retorno
def exemplo3(a):
    triplo = a * 3

    return triplo
def exemplo4(num):

    if num % 2 == 0:
        return num**2
    else :
        n = num**3
        return n

k = exemplo4(852)
print("Resposta:", k)
