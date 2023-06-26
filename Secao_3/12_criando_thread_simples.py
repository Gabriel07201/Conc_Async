import threading
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))

    th.start()

    print('Para mostrar outras coisas executando...')
    print('Algo vezes dois' * 2)

    th.join()
    
    print('Pronto')

def contar(o_que, numero):
    for n in range(1, numero+1):
        print(f'{n} {o_que}')
        time.sleep(1)

if __name__ == '__main__':
    main()