import threading
import time
                        # CONCORRENCIA x PARALELISMO

contador = 0
max_for = 10000000
paralelo = True

# lock = threading.Lock()

def somar():
    global contador
    for i in range(0, max_for):
        # lock.acquire()     #o t2 vai aguardar o t1 dar o release para executar
        contador +=1
        # lock.release()

start_time = time.time()
if paralelo:
    t1 = threading.Thread(target=somar)
    t2 = threading.Thread(target=somar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
else:
    somar()
    somar()

end_time = time.time() - start_time
print('time = %f'% (end_time))
print('contador %d' %(contador))

# time = 1.384945
# contador 12101337