#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def make_exponentiation(a, b):
    if isinstance(a, float) and isinstance(b, float):
        struct = Exponentiation(a, b)

        return struct
    else:
        raise ValueError


class Exponentiation:

    def __init__(self, first=0.0, second=0.0):
        first = float(first)
        second = float(second)

        self.__number = first
        self.__exponent = second

        if first < 0:
            raise ValueError

    @property
    def number(self):
        return self.__number

    @property
    def exponent(self):
        return self.__exponent

    def read(self):
        line = input('Введите: ')
        parts = list(line.split('^', maxsplit=1))

        if "," in line:
            raise ValueError
        elif "/" in line:
            num_exp = []
            for part in parts:
                temp = list(map(int,part.split('/', maxsplit=1)))
                num_exp.append(temp[0]/temp[1])

            self.__number = num_exp[0]
            self.__exponent = num_exp[1]
        else:
            self.__number = float(parts[0])
            self.__exponent = float(parts[1])

    def display(self):
        print(f"{self.__number}^{self.__exponent}")

    def power(self):
        return math.pow(self.number, self.exponent)


if __name__ == '__main__':
    e1 = make_exponentiation(1/2, 1/5)
    e1.display()

    e1.read()
    e1.display()

    e2 = make_exponentiation(0.5, 0.2)
    print(e2.power())
