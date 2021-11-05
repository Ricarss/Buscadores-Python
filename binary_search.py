import time as t
import numpy.random as rd

def ar_gen():
    
    size = rd.randint(10000,50000) # código que genera el tamaño de la lista
    ar = [rd.randint(0,size) for i in range(size)] # código que genera el listado 

    return ar

def linear_search(ar,obj):

    match = False

    for i in ar:
        if i == obj:
            match = True
            break
    
    return match

def binary_search(ar,obj,ini,end):

    if ini > end:
        return False

    medio = (end-ini) // 2

    if ar[medio] == obj:
        return True
    
    if ar[medio] > obj:
        return binary_search(ar,obj,medio+1,end)
    
    if ar[medio] < obj:
        return binary_search(ar,obj,ini,medio-1)

if __name__ == '__main__':
    
    ar = ar_gen()
    obj = rd.randint(0,55000)

    inicio = t.time()
    print(f"""
    {obj} {"está" if linear_search(ar,obj) else "no está"} en la lista generada
    """)
    fin = t.time()
    
    print(f'''
    La búsqueda lineal tardó {fin-inicio} segundos    
    ''')

    print("\n")

    inicio = t.time()
    print(f'''
    {obj} {'está' if binary_search(ar,obj,0,len(ar)-1) else 'no está'} en la lista generada
    ''')
    fin = t.time()

    print(f'''
    La búsqueda binaria tardó {fin - inicio} segundos
    ''')

