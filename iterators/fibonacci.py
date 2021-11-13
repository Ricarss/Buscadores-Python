import time

# Iterator 
class Fibon():
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):

        if self.counter == 0: #primera iteración 
            
            self.counter += 1 # contador sigue de 0 -> 1
            return self.n1

        elif self.counter == 1: #segunda iteración

            self.n1 = self.n2 # primer elemento pasa a ser segundo elemento (1,1)
            self.counter += 1 # contador sigue de 1 -> 2
            return self.n2

        else: 

            self.aux = self.n1 + self.n2 # auxiliar almacena suma para luego pasarla a 2
            self.n1 = self.n2 # se cambia el primer elemento por el seegundo
            self.n2 = self.aux # el segundo elemento toma el valor de la suma (contenida en el auxiliar)
            self.counter += 1 # el contador continúa con el mismo procedimiento
            return self.n2

# Generator

def fib_gen(max):

    n1 = 0
    n2 = 1
    ncount = 0

    while ncount < max:

        if ncount == 0:

            ncount +=1 
            yield n1

        elif ncount == 1:

            n1 = n2
            ncount +=1

            yield n2
        
        else:

            aux = n1 + n2
            n1 = n2
            n2 = aux
            ncount += 1

            yield n2


if __name__ == '__main__':
    for element in fib_gen(int(input('Inserte un máximo: \n'))):
        print(element)
        time.sleep(0.5)
