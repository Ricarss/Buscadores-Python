import random as rd

def steal(objects,morral,c_morral):
    
   if len[objects]   
    


class Objects():

    def __init__(self,name,weight,value):
        
        self.name = name
        self.weight = int(weight)
        self.value = int(value)

    def get(self):

        return {'name':self.name, 'weight':self.weight,'value':self.value}

def articles(): 
    
    articles = [
            
            Objects(
                name = f'Objeto {i+1}', # Se nombrará el objeto según su posición del array
                weight = rd.randint(1000,2000), # Generación aleatoria del peso del artículo
                value = rd.randint(100,3500) # Generación aleatoria del valor del artículo
            ).get()  
            
            for i in range(0,29)
            
            ]

    return articles # se regresa el array de diccionarios que contienen la información de cada objeto

if __name__ == '__main__':

    morral = {}
    c_morral = rd.randint(10000,15000) # Generación aleatoria de la capacidad límite de carga para el morral
    print(f'La carga máxima del morral es de: {c_morral}')
    
    objects = articles()
    
    morral = steal(objects,morral, c_morral)

