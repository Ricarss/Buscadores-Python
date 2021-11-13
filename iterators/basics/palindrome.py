def is_palindrome(word: str) -> bool:
    """" Función especial para validar si una cadena de texto recibida es un palíndromo (puede leerse lo mismo de derecho y al revés) """
    word = word.lower().replace(" ","").replace("á","a").replace("é","e").replace("ú","u").replace("í","i").replace("ó","o")

    return word == word[::-1]




if __name__ == '__main__':
    print(is_palindrome('aná'))