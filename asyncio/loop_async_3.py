import queue

contador = 0
max_for = 10000000 // 1000
# max_for = 100



#------------------EXEMPLO SEM CONCORRENCIA-----------------
# def somar():
#     global contador
#     for i in range(0,max_for):
#         contador += 1
#         yield
#
# for _ in somar():
#     pass
#
# for _ in somar():
#     pass
#
# print(contador)

# #--------------EXEMPLO FILA 'queue' -----------------------

def somar_1000(tarefa):
    yield
    global contador
    print('Executing {}'.format(tarefa))
    for i in range(0, 1000):
        contador += 1

def somar(tarefa):
    global contador
    for i in range(0,max_for):
        print('Executing {}'.format(tarefa))
        contador += 1
        yield somar_1000('somar_1000_{}'.format(tarefa))

q = queue.Queue()       # FIFO (First in first out)
q.put(somar('tarefa_1'))
q.put(somar('tarefa_2'))


while not q.empty():
    tarefa = q.get()
    # next(tarefa) #--
    try:
        fn = next(tarefa)
        if fn:
            q.put(fn)
    except StopIteration:
        pass
    else:
        q.put(tarefa)

print(contador)