from datetime import date, datetime

def exec_t(func):
    def wrapper(*args,**kwargs):
        i_time = datetime.now()
        func(*args,**kwargs)
        f_time = datetime.now()

        print(f'Tiempo de ejecución: {f_time - i_time} segundos')

    return wrapper

@exec_t
def rand_func():

    for _ in range(1,10000):
        pass


if __name__ == '__main__':
    rand_func()
