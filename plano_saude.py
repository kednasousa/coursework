print('Bem vindo ao Sistema de Kedna Cleia')

valorBase = float(input('Informe o valor Base do plano: '))
idade = int(input('Informe a idade do cliente: '))

if idade >= 0 and idade < 19:
    porcentagem = 100
elif idade >= 19 and idade < 29:
    porcentagem = 150
elif idade >= 29 and idade < 39 :
    porcentagem = 225
elif idade >= 39 and idade < 49 :
    porcentagem = 240
elif idade >= 49 and idade < 59 :
    porcentagem = 350
else :
    porcentagem = 600

valorMensal = valorBase * (porcentagem / 100)

print(f'O valor mensal do plano para idade de {idade} anos é de: R$ {valorMensal:.2f}')