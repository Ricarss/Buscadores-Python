import random as rd

def ar_gen():
    
    size = rd.randint(5,10) # código que genera el tamaño de la lista
    ar = [rd.randint(0,size) for i in range(size)] # código que genera el listado 

    return ar

def bub_sort(ar):
    
    bubble = 0
    move = len(ar)

    for idx1 in range(move):
        
        ar_bub = ar[0:move-idx1]
        
        for idx2 in range(len(ar_bub)-1) :

            if ar[idx2] > ar[idx2+1]:

                bubble = ar[idx2+1]
                ar[idx2+1] = ar[idx2]
                ar[idx2] = bubble                

    return ar

if __name__ == '__main__':
    ar = ar_gen()
    print(f'El arreglo a ordenar es: \n {ar} \n')
    print(f'El arreglo ordenado es: \n {bub_sort(ar)}')

