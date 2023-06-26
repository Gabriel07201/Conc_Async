import datetime
import math

import threading
import multiprocessing

def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'qtd_cores: {qtd_cores}')

    inicio = datetime.datetime.now()

    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) // qtd_cores
        fim = 50_000_000 * n // qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        threads.append(
            threading.Thread(target=computar, kwargs={'inicio': ini, 'fim': fim})
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio
    print(tempo)


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()


# 0.785 - tempo performance padrao