#-*- coding: utf-8 -*-
import random


def run():
    number_found = False
    random_number = random.randint(0, 20) # genera un numero randomico que sea entre 0 y 20 sin incluir 20

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Muy bien, Encontraste el numero')
            number_found = True
        elif number > random_number:
            print('el numero es MENOR que el que dijitó')
        else: 
            print('El numero es MAYOR que el que dijitó')


if __name__ == "__main__":
    run()