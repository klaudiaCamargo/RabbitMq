import random
                    #  como funciona o FOR

# def lancar_dados(n):
#     dados = []          #   usar essa lista para guardar os dados
#     for i in range(0, n):
#         dados.append(random.randint(1, 6))
#     return dados
#
# for dado in lancar_dados(10):
#     print(dado)

#----------------- ITERATOR -----------------------------

class LancarDados(object):
    def __init__(self, n):
        self.n = n
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < self.n:
            self.cursor += 1
            return random.randint(1,6)
        else:
            raise StopIteration

# for dado in LancarDados(10):
#     print(dado)

#----------------- GENERATOR yield-----------------------------

def lancar_dados(n):
    print('Funcao iniciada')
    for i in range(0, n):
        print('entrou no for')
        yield random.randint(1, 6)  #   quando tem o yield a um bloqueio de execucao até ser chamado um __next__
        print('saiu do for')
    print('fim da funcao')

for dado in lancar_dados(2):
    print(dado)

dados = lancar_dados(2)
print(dados)