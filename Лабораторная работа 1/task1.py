from typing import Union
import doctest

class Automobile:
    def __init__(self, color_of_the_car: str, width_of_the_car: Union[int, float], length_of_the_car: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param color_of_the_car: Цвет автомобиля
        :param width_of_the_car: Ширина автомобиля
        :param length_of_the_car: Длина автомобиля

        Примеры:
        >>> automobile = Automobile("Красный", 1.5, 4) # инициализация экземпляра класса
        """
        if not isinstance(color_of_the_car, str):
            raise TypeError("Цвет автомобиля должен быть описан текстом (тип данных str)")
        self.color_of_the_car = color_of_the_car

        if not isinstance(width_of_the_car, (int, float)):
            raise TypeError("Ширина автомобиля должна быть типа int или float")
        if width_of_the_car <= 0:
            raise ValueError("Ширина автомобиля должна быть положительным числом")
        self.width_of_the_car = width_of_the_car

        if not isinstance(length_of_the_car, (int, float)):
            raise TypeError("Длина автомобиля должна быть типа int или float")
        if length_of_the_car <= 0:
            raise ValueError("Длина автомобиля должна быть положительным числом")
        self.length_of_the_car = length_of_the_car

    def color_check(self, the_first_color: str, the_second_color: str) -> bool:
        """
        Функция, которая проверяет, является ли хотя бы один из двух предложенных цветов цветом рассматриваемой машины

        :param the_first_color: Первый цвет
        :param the_second_color: Второй цвет

        :return: Совпадает ли исходный цвет хотя бы с одним из предложенных?

        Примеры:
        >>> automobile = Automobile("Красный", 1.5, 4)
        >>> automobile.color_check("Синий", "Красный")
        """
        if not isinstance(the_first_color, str):
            raise TypeError("Предложенный цвет автомобиля должен быть описан текстом (тип данных str)")

        if not isinstance(the_second_color, str):
            raise TypeError("Предложенный цвет автомобиля должен быть описан текстом (тип данных str)")
        ...

    def parking_capacity(self, parking_width: Union[int, float], parking_length: Union[int, float]) -> bool:
        """
        Функция, которая проверяет - вмещается ли автомобиль на машино-место определённых размеров

        :param parking_width: Ширина парковочного места
        :param parking_length: Длина парковочного места

        :return: Вмещается ли автомобиль на машино-место?

        Примеры:
        >>> automobile = Automobile("Красный", 1.5, 4)
        >>> automobile.parking_capacity(3, 6)
        """
        if not isinstance(parking_width, (int, float)):
            raise TypeError("Ширина машино-места должна быть типа int или float")
        if parking_width <= 0:
            raise ValueError("Ширина машино-места должна быть положительным числом")

        if not isinstance(parking_length, (int, float)):
            raise TypeError("Длина машино-места должна быть типа int или float")
        if parking_length <= 0:
            raise ValueError("Длина машино-места должна быть положительным числом")
        ...

class Frame:
    def __init__(self, width_of_the_frame: int, length_of_the_frame: int):
        """
        Создание и подготовка к работе объекта "Рамка"

        :param width_of_the_frame: Ширина рамки
        :param length_of_the_frame: Длина рамки

        Примеры:
        >>> frame = Frame(15, 25) # инициализация экземпляра класса
        """
        if not isinstance(width_of_the_frame, int):
            raise TypeError("Ширина рамки должна быть типа int")
        if width_of_the_frame <= 0:
            raise ValueError("Ширина рамки должна быть положительным числом")
        self.width_of_the_frame = width_of_the_frame

        if not isinstance(length_of_the_frame, int):
            raise TypeError("Длина рамки должна быть типа int")
        if length_of_the_frame <= 0:
            raise ValueError("Длина рамки должна быть положительным числом")
        self.length_of_the_frame = length_of_the_frame

    def frame_area(self) -> int:
        """
        Функция, которая считает площадь рамки

        :return: Площадь рамки

        Примеры:
        >>> frame = Frame(15, 25)
        >>> frame.frame_area()
        375
        """
        return self.width_of_the_frame * self.length_of_the_frame

    def perimeter_of_the_frame(self) -> int:
        """
        Расчёт периметра рамки

        :return: Периметр рамки

        Примеры:
        >>> frame = Frame(15, 25)
        >>> frame.perimeter_of_the_frame()
        80
        """
        return (self.width_of_the_frame + self.length_of_the_frame) * 2

class Box:
    def __init__(self, length: int, width: int, height: int):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param length: Длина коробки
        :param width: Ширина коробки
        :param height: Высота коробки

        Примеры:
        >>> box = Box(10, 20, 30) # инициализация экземпляра класса
        """
        if not isinstance(length, int):
            raise TypeError("Длина коробки должна быть типа int")
        if length <= 0:
            raise ValueError("Длина коробки должна быть положительным числом")
        self.length = length

        if not isinstance(width, int):
            raise TypeError("Ширина коробки должна быть типа int")
        if width <= 0:
            raise ValueError("Ширина коробки должна быть положительным числом")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("Высота коробки должна быть типа int")
        if height <= 0:
            raise ValueError("Высота коробки должна быть положительным числом")
        self.height = height

    def bottom_area(self) -> int:
        """
        Определение площади дна коробки

        :return: Площадь дна коробки

        Примеры:
        >>> box = Box(10, 20, 30)
        >>> box.bottom_area()
        200
        """
        return self.width * self.length

    def box_volume(self) -> int:
        """
        Определение объёма коробки

        :return: Объём коробки

        Примеры:
        >>> box = Box(10, 20, 30)
        >>> box.box_volume()
        6000
        """
        return self.width * self.length * self.height

if __name__ == "__main__":
    doctest.testmod()
# перенос строки
