import random as rd

if __name__ == '__main__':
    pass

def ar_gen():
    
    size = rd.randint(1000,1500) # código que genera el tamaño de la lista
    ar = sorted([rd.randint(0,size) for i in range(size)]) # código que genera el listado 

    return ar


def bub_sort(ar):
    pass

