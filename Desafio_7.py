# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00
def calcula_gorjeta(valor_conta, qualidade_serviço):
    if qualidade_serviço == 'ruim':
        gorjeta = valor_conta * 0
        print(f'A qualidade do serviço foi {qualidade_serviço}, com isso a gorjeta será de {gorjeta:.2f}')
    elif qualidade_serviço == 'médio':
        gorjeta = valor_conta * 0.025
        print(f'A qualidade do serviço foi {qualidade_serviço}, com isso a gorjeta será de {gorjeta:.2f}')
    elif qualidade_serviço == 'bom':
        gorjeta = valor_conta * 0.04
        print(f'A qualidade do serviço foi {qualidade_serviço}, com isso a gorjeta será de {gorjeta:.2f}')
    else:
        gorjeta = valor_conta * 0.05
        print(f'A qualidade do serviço foi {qualidade_serviço}, com isso a gorjeta será de {gorjeta:.2f}')

calcula_gorjeta(100,'ruim')
calcula_gorjeta(100,'médio')
calcula_gorjeta(100,'bom')
calcula_gorjeta(100,'exelente')



