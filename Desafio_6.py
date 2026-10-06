# Crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseado no periodo do dia
# Periodos :    Manhã: 5 até 12, Tarde: 13 até 18, Noite: 18 até 24

# Exemplo: 
# Nome: Allana
# Hora : 9
# Bom dia, Allana

# Exemplo2: 
# Nome: Gustavo B
# Hora : 15
# Boa Tarde, Gustavo B

nome = ["Allana", "Gustavo B", "Rian"]

def cumprimentar(nome, horas):
    if horas >=5 and horas <= 12:
        print(f"Bom Dia {nome}")
    elif horas <= 18:
        print(f"Boa Tarde {nome}")
    else:
        print(f"Boa noite {nome}")

cumprimentar(nome[0], 9)
cumprimentar(nome[1], 15)
cumprimentar(nome[2], 21)