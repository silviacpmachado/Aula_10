# Calcula média de notas
# Não sabemos quantos alunos, mas todos terão 4 notas sempre.


# contador = 1
# #resposta = 'S'
# while True:
#     print('Olá')

#     opcao = input('Deseja calcular para outro aluno? ').strip().upper()
#     if opcao != 'S':
#         break 


def calcula_media(lista_notas):
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med


contador = 1
# #resposta = 'S'
while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do aluno: ')

    notas = []
    try:
        for i in range(4):
            nota = float(input('Informe a nota: '))
            notas.append(nota)
    except ValueError:
        print('Erro: informe apenas valores válidos!')
    else:
        total, media = calcula_media(notas)

        print('\nRESULtado')
        print(f'Aluno: {aluno}')
        print(f'Total de Pontos: {total}')
        print(f'Média: {media:.2f}')

    finally:
        print('Processo encerrado para o aluno')


    opcao = input('Deseja calcular para outro aluno? ').strip().upper()
    if opcao != 'S':
        break

contador += 1