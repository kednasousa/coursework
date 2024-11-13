# Meu nome
nome = 'Kedna Cleia'

# Cardápio da pizzaria
cardapio = ('''
+-------------------------------------------------+
| ---- Cardápio da Pizzaria da {} ------ |
+----------+-------------------+------------------+
| Tamanho  | Pizza Salgada (PS)| Pizza Doce (PD)  |
+----------+-------------------+------------------+
|    P     |      R$ 30,00     |      R$ 34,00    |
|    M     |      R$ 45,00     |      R$ 48,00    |
|    G     |      R$ 60,00     |      R$ 66,00    |
+----------+-------------------+------------------+
'''.format(nome))
print(cardapio)

# Preços das pizzas
precos = {
    ('PS', 'P'): 30,
    ('PD', 'P'): 34,
    ('PS', 'M'): 45,
    ('PD', 'M'): 48,
    ('PS', 'G'): 60,
    ('PD', 'G'): 66
}

# Inicializa o valor total do pedido
valor_total = 0

# Loop principal para receber os pedidos
while True:
    # Solicita o sabor da pizza
    sabor = input("Insira o sabor desejado (PS/PD): ").upper()
    if sabor not in ['PS', 'PD']:
        print("Sabor inválido. Tente novamente")
        continue

    # Solicita o tamanho da pizza
    tamanho = input('Insira o tamanho desejado (P/M/G): ').upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente')
        # Solicita novamente até que um tamanho válido seja inserido
        while tamanho not in ['P', 'M', 'G']:
            tamanho = input('Insira o tamanho desejado (P/M/G): ').upper()
        continue

    # Calcula o preço da pizza selecionada
    preco = precos[(sabor, tamanho)]
    valor_total += preco
    print(f'Você pediu uma Pizza {sabor} no tamanho {tamanho}: R$ {preco:.2f}')

    # Pergunta se o cliente deseja continuar pedindo
    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if continuar != 'S':
        print(f"O valor total do seu pedido é: R$ {valor_total:.2f}")
        break