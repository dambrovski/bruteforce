import random
import time


print("Bem vindo ao Sistema de BruteForce Wifi 2015")

#Sistema criado para quebrar passwords de wifi de 8 digitos, apenas digitos numericos de 0 - 9
#ou seja, sao 8^8 que sao 16777216 (dezesseis milhões setecentos e setenta e sete mil duzentos e dezesseis) possibilidades
#o programa tem fins de mensurar o tempo que a  maquina levaria para quebrar essa senha

password = '99999999'

test = '0'
listPasswordTesteds = []
listPasswords = []

#gerar senhas a serem testadas

start = time.time()


for p in range(0, 500):
    num = random.randint(10000000, 99999999)
    if(num in listPasswords):
        pass
    else:
        listPasswords.append(num)
end = time.time()
x = len(listPasswords)

print(x)
print("Tempo que levou para quebrar password no pior dos casos: ")
print(end - start)



