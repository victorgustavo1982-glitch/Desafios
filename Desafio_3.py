# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....

tabuada = int(input("Digite qualquer número: "))
for num in range(0,11):
    print(f"{tabuada} x {num} = {tabuada*num}")