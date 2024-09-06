#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 2
Создать класс ModelWindow для работы с моделями экранных окон.
В качестве полей задаются: заголовок окна, координаты левого верхнего угла,
размер по горизонтали, размер по вертикали, цвет окна,
состояние «видимое/невидимое», состояние «с рамкой/без рамки».
Координаты и размеры указываются в целых числах.
Реализовать операции: передвижение окна по горизонтали,по вертикали;
изменение высоты и/или ширины окна изменение цвета;
изменение состояния, опрос состояния. Операции передвижения и изменения размера
должны осуществлять проверку на пересечение границ экрана.
Функция вывода на экран должна индуцировать состояние полей объекта.
В раздел программы, начинающийся после инструкции if __name__ = '__main__':
добавить код, демонстрирующий возможности разработанного класса.
"""

WIN_WIDTH = 1920
WIN_HEIGHT = 1080


class ModelWindow:
    fields = [
        ("Заголовок: ", str),
        ("Цвет: ", str),
        ("Координата по x: ", int),
        ("Координата по y: ", int),
        ("Ширина: ", int),
        ("Высота: ", int),
        ("Видимость (yes/no): ", str),
        ("Рамка (yes/no): ", str),
    ]

    def __init__(
        self,
        title="New window",
        color="white",
        x=0,
        y=0,
        width=500,
        height=500,
        vis="yes",
        border="yes",
    ):
        self.__title = title
        self.__color = color
        self.__coord_x = x
        self.__coord_y = y
        self.__width = width
        self.__height = height
        self.__visibility = vis
        self.__border = border

    def move_x(self, x=0):
        if (
            self.__coord_x + self.__width + x <= WIN_WIDTH
            and self.__coord_x + x >= 0
        ):
            self.__coord_x += x
        else:
            print("Окно пересекает границы экрана")

    def move_y(self, y=0):
        if (
            self.__coord_y + self.__height + y <= WIN_HEIGHT
            and self.__coord_y + y >= 0
        ):
            self.__coord_y += y
        else:
            print("Окно пересекает границы экрана")

    def change_size(self, w=0, h=0):
        if self.__width + w >= 0 and self.__height + h >= 0:
            if (
                self.__coord_x + self.__width + w <= WIN_WIDTH
                and self.__coord_y + self.__height + h <= WIN_HEIGHT
            ):
                self.__width += w
                self.__height += h
            else:
                print("Окно пересекает границы экрана")
        else:
            print("Ширина/высота не может быть отрицательной")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visability(self, condition):
        self.__visibility = condition

    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, condition):
        self.__border = condition

    def read(self):
        values = []
        for field_name, field_type in ModelWindow.fields:
            user_input = input(f"Введите {field_name}")
            if not user_input.isdigit() and field_type == str:
                values.append(field_type(user_input))
            elif user_input.isdigit() and field_type == int:
                values.append(field_type(user_input))
            else:
                raise TypeError

        i = 0
        for key in self.__dict__.keys():
            object.__setattr__(self, key, values[i])
            i += 1

    def display(self):
        print("\n")
        i = 0
        for value in self.__dict__.values():
            print(f"{ModelWindow.fields[i][0]}{value}")
            i += 1


if __name__ == "__main__":
    w1 = ModelWindow("My window", "blue", 100, 100, 1280, 720)
    w1.display()

    w1.color = "green"
    w1.visability = "no"
    w1.border = "no"
    print(f"Цвет:{w1.color}, видимость:{w1.visibility}, рамка:{w1.border}\n")

    w = ModelWindow()
    w.read()
    w.display()

    w.change_size(120, -50)
    w.move_x(-240)
    w.move_y(60)
    w.display()
