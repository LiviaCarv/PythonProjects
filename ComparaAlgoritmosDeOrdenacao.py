import random
import time
import AlgoritmosDeOrdenacao

class conta_tempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]

        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        o = AlgoritmosDeOrdenacao.Ordenador()
        antes = time.time()
        o.bubblesort(lista1)
        depois = time.time()
        print(f'Bolha demorou {depois-antes} segundos.')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Seleção direta demorou {depois - antes} segundos.')

        antes = time.time()
        o.bubblesortMelhorado(lista3)
        depois = time.time()
        print(f'Bolha melhorado demorou {depois - antes} segundos.')


conta_tempos().compara(1000)