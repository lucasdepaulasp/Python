def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_Maria_do_Jurunas, candidato_Jose_da_Silva, candidato_Joao_do_Tapana
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '1' or candidato == '2' or candidato == '3':
            if candidato == '1':
                candidato_Jose_da_Silva += 1
            elif candidato == '2':
                 candidato_Maria_do_Jurunas += 1
            elif candidato == '3':
                 candidato_Joao_do_Tapana += 1
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato= str(input('Digite um numero valido para o candidato: '))
            votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global candidato_Maria_do_Jurunas, candidato_Jose_da_Silva, candidato_Joao_do_Tapana

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO JOSÉ DA SILVA - TOTAL DE ' + str(candidato_Jose_da_Silva))
    print('CANDIDATO MARIA DO JURUNAS - TOTAL DE ' + str(candidato_Maria_do_Jurunas))
    print('CANDIDATO JOÃO DO TAPANÃ - TOTAL DE ' + str(candidato_Joao_do_Tapana))

    exit()  # encerra prog


if __name__ == '__main__':  # funcao main 
    candidato_Maria_do_Jurunas = 0
    candidato_Jose_da_Silva = 0
    candidato_Joao_do_Tapana = 0

    while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
        candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o numero do seu candidato: '))
        votacao(candidato)