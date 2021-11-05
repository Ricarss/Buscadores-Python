import time as t
import numpy.random as rd

def ar_gen():
    
    size = rd.randint(10000,50000) # código que genera el tamaño de la lista
    ar = [rd.randint(0,size) for i in range(size)] # código que genera el listado 

    return ar

def linear_search(ar,obj):

    match = False
    steps = 0

    for i in ar:
        steps += 1
        if i == obj:
            match = True
            break
    
    return match, steps

def binary_search(ar,obj,ini,end,steps):

    steps += 1

    if ini > end:
        return False, steps

    medio = (end-ini) // 2

    if ar[medio] == obj:
        return True, steps
    
    if ar[medio] > obj:
        return binary_search(ar,obj,medio+1,end,steps)
    
    if ar[medio] < obj:
        return binary_search(ar,obj,ini,medio-1,steps)

if __name__ == '__main__':
    
    ar = ar_gen()
    obj = rd.randint(0,55000)
    
    ls_ini = t.time()
    ls_match, ls_steps = linear_search(ar,obj)
    ls_time = t.time() - ls_ini

    bs_ini = t.time()
    bs_match, bs_steps = binary_search(ar,obj,0,len(ar)-1,0)
    bs_time = t.time() - bs_ini

    print(f"""
    {obj} {"está" if ls_match else "no está"} en la lista generada
    """)
    
    print(f'''
    La búsqueda lineal tardó {ls_time} segundos, con un total de {ls_steps} pasos
    ''')

    print("\n")

    inicio = t.time()
    print(f'''
    {obj} {'está' if bs_match else 'no está'} en la lista generada
    ''')
    fin = t.time()

    print(f'''
    La búsqueda binaria tardó {bs_time} segundos, con un total de {bs_steps} pasos
    ''')
