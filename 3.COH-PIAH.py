import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatorio = 0
    for i in range(6):
        somatorio += abs(as_a[i] - as_b[i])
    a = somatorio / 6
    return a

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sent = separa_sentencas(texto)
    lista_frases = []
    for i in sent:
        lista_frases.append(separa_frases(i))
    palavras = []
    for a in lista_frases:
        for b in a:
            palavras.append(separa_palavras(b))
    palavras_diferentes = []
    palavras_unicas = []
    for a in palavras:
        for b in a:
            palavras_diferentes = n_palavras_diferentes(b)
            palavras_unicas = n_palavras_unicas(b)
    #TAMANHO MEDIO
    tamanho_palavras = 0
    cont = 0
    for a in palavras:
        for b in a:
            tamanho_palavras += len(b)
            cont += len(b)
    tamanho_medio_palavras = tamanho_palavras/cont
    #TYPE-TOKEN
    type_token = palavras_diferentes/cont
    #HAPAX
    hapax = palavras_unicas/cont
    #TAMANHO MEDIO DE SENTENÇA
    tamanho_sentenca = 0
    cont_sent = 0
    for a in sent:
        tamanho_sentenca += len(a)
    media_sentenca = tamanho_sentenca/len(sent)
    #COMPLEXIDADE
    num_frases = len(lista_frases)
    complexidade = num_frases/len(sent)
    #TAMANHO MEDIO DE FRASE
    caract_frase = 0
    for a in lista_frases:
        for b in a:
            caract_frase += len(b)
    media_frase = caract_frase/num_frases
    return [tamanho_medio_palavras, type_token, hapax, media_sentenca, complexidade, media_frase]



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    comparacao = []
    for i in textos:
        ass = calcula_assinatura(i)
        assinaturas.append(ass)
    for i in assinaturas:
        comp = compara_assinatura(ass_cp, i)
        comparacao.append(comp)
    ind = comparacao.index(min(comparacao))
    return ind+1


def main():
    assinatura = le_assinatura()
    textos = le_textos()

    return print("O autor do texto ", avalia_textos(textos, assinatura), " está infectado com COH-PIAH")

main()