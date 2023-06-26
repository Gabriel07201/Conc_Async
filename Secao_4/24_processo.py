import multiprocessing


def faz_algo(valor):
    print('Fazendo algo com o: ', valor)



def main():
    print(f'Início do processo: {multiprocessing.current_process().name}')
    pc = multiprocessing.Process(target=faz_algo, args=('batata',), name='Processo batata')

    print(f'Iniciando outro processo: {pc.name}')

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()