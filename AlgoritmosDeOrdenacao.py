
class Ordenador:
    def selecao_direta(self, lista):
        tam = len(lista)

        # O primeiro laço pega o primeiro elemento e o supõe como mínimo
        # O segundo laço compara esse elemento com todos elementos com indices maiores
        for i in range(tam):
            posicao_do_menor = i

            for j in range(i + 1, tam):
                if lista[j] < lista[posicao_do_menor]:
                    posicao_do_menor = j

            lista[i], lista[posicao_do_menor] = lista[posicao_do_menor], lista[i]
        return lista


    def bubblesort(self, lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    #Bubblesort melhorado
    #Ao nao identificar trocas em uma iteração, a lista ja esta ordenada
    #Break na iteração que nao teve trocas

    def bubblesortMelhorado(self, lista):
        fim = len(lista) -1
        while fim >= 0:
            for j in range(fim):
                trocas = 0
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas += 1
            if trocas == 0:
                break
            fim -= 1

        return lista