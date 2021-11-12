def steal(morral, c_morral, objects):
    pass

class Objects():

    def __init__(self,n,w,v):
        
        self.name = n
        self.weight = float(w)
        self.value = float(v)

    def get(self):

        return {'name':self.name, 'weight':self.weight,'value':self.value}

def articles():

    pass
    

if __name__ == '__main__':

    morral = {}
    c_morral = 100

    print(f'{Objects("Objeto 1",100,100).get()}')

