def multiplier(n:int):

    assert type(n) == int, "Solo puedes trabajar con números"

    def printer(word:str)->str:

        assert type(word) == str, "Solo puedes trabajar con cadenas de texto"
        n_word = word * n

        return n_word

    return printer

def run():
    
    printer2 = multiplier(2)
    printer3 = multiplier(3)

    print(printer2('hola'))
    print(printer3('chau'))

if __name__ == '__main__':
    run()