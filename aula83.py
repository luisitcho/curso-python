# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for pergunta in perguntas:
    print("----------------------------------------")
    print(f"Pergunta: {pergunta['Pergunta']}")
    print("----------------------------------------")
    print('Opções')

    for indice, opcao in enumerate(pergunta['Opções']):
        print(f"{indice}) {opcao}")

    resposta = input('Escolha uma opção: ')

    if resposta.isdigit():
        resposta_int = int(resposta)
        
        try:
            alternativa = pergunta['Opções'][resposta_int]
            alternativa_correta = pergunta['Resposta']
            
            if alternativa == alternativa_correta:
                print("Resposta correta!")
                acertos += 1
            else:
                print(f"Resposta errada! A resposta correta era: {alternativa_correta}")
        
        
        except Exception as e:
            print('Resposta não encontrada!')
            
    else:
        print("Por favor, digite um número válido.")
        
print(f"Total de acertos: {acertos}")


# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')