# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9

num = int(input("Digite um número: "))
sucessor = num + 1
antecessor = num - 1

print(f"Voce digitou o numero : {num}")
print(f"O sucessor dele é o número : {sucessor}")
print(f"O antecessor dele é o número : {antecessor}")