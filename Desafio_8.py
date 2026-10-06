# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

def pode_ver_filme(idade, classificação):
    if classificação == 'L (Livre)' :
        print(f"A classificação do filme é de: {classificação} L (Livre)")
    elif classificação == 'Maior de 12' and idade >=12 :
        print(f"A classificação do filme é de: {classificação} Maior de 12, pode assistir")
    elif classificação == 'Maior de 14' and idade >=14:
        print(f"A classificação do filme é de: {classificação} Maior de 14, pode assistir")
    elif classificação == 'Maior 16' and idade >= 16 and idade <18:
        print(f"A classificação do filme é de: {classificação} Maior de 16, pode assistir")

    elif classificação == 'Maior de 18' and idade >=18:
          print(f"A classificação do filme é de: {classificação} Maior de 18, pode assistir")
           
    else:
        print(f'Não Pode assitir')
      

pode_ver_filme(0, 'L (Livre)')
pode_ver_filme(12,'Maior de 12')
pode_ver_filme(14, 'Maior de 14')
pode_ver_filme(16, 'Maior 16')
pode_ver_filme(18, 'Maior de 18')
pode_ver_filme(12, 'Maior de 18')