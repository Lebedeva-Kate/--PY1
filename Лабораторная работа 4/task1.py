if __name__ == "__main__":

    class House:
        """ Базовый класс дома. """
        def __init__(self, name_of_the_complex: str, floor_area: float, number_of_floors: int):
            """
            Создание и подготовка к работе объекта "Дом"

            :param name_of_the_complex: Название жилого комплекса
            :param floor_area: Площадь этажа
            :param number_of_floors: Количество этажей
            """

            if not isinstance(name_of_the_complex, str):
                raise TypeError("Атрибут name_of_the_complex должен иметь тип str")
            self._name_of_the_complex = name_of_the_complex

            if not isinstance(floor_area, float):
                raise TypeError("Атрибут floor_area должен иметь тип float")
            if floor_area <= 0:
                raise ValueError("Атрибут floor_area должен быть положительным числом")
            self.floor_area = floor_area

            if not isinstance(number_of_floors, int):
                raise TypeError("Атрибут number_of_floors должен иметь тип int")
            if not 1 <= number_of_floors <= 3:
                raise ValueError("Атрибут number_of_floors должен иметь значение в промежутке от 1 до 3")
            self.number_of_floors = number_of_floors

        @property
        def name_of_the_complex(self) -> str:
            """
            Защищаем атрибут, поскольку хотим, чтобы он не изменялся для всех экземпляров класса

            :return: Состояние атрибута name_of_the_complex
            """
            return self._name_of_the_complex

        def total_area(self) -> float:
            """
            Функция, которая считает общую площадь всего дома со всеми входящими в него блоками

            :return: Площадь дома
            """
            return self.floor_area * self.number_of_floors

        def belonging_to_the_complex(self, input_name: str) -> bool:
            """
            Функция, которая проверяет входит ли данный дом в указанный жилой комплекс

            :param input_name: Введённое пользователем название комплекса

            :return: Входит ли дом в указанный жилой комплекс
            """
            if not isinstance(input_name, str):
                raise TypeError("Аргумент input_name должен иметь тип str")
            return self.name_of_the_complex == input_name

        def __str__(self) -> str:
            """
            Определяет поведение функции str(), вызванной от экземпляра класса House

            :return: f-string
            """
            return f"Жилой комплекс: {self.name_of_the_complex}. Площадь этажа дома: {self.floor_area}. Количество этажей: {self.number_of_floors}."

        def __repr__(self) -> str:
            """
            Определяет поведение функции repr(), вызванной от экземпляра класса House

            :return: f-string
            """
            return f"{self.__class__.__name__}(name_of_the_complex={self.name_of_the_complex!r}, floor_area={self.floor_area!r}, number_of_floors={self.number_of_floors!r})"

    class Duplex(House):
        """ Дочерний класс дома. """
        def __init__(self, name_of_the_complex: str, floor_area: float, number_of_floors: int, increasing_coef: float):
            """
            Создание и подготовка к работе объекта "Дуплекс"

            :param name_of_the_complex: Название жилого комплекса
            :param floor_area: Площадь этажа
            :param number_of_floors: Количество этажей
            :param increasing_coef: Повышающий коэффициент для площади дома
            """
            super().__init__(name_of_the_complex, floor_area, number_of_floors)

            if not isinstance(increasing_coef, float):
                raise TypeError("Атрибут increasing_coef должен иметь тип float")
            if not 1 <= increasing_coef <= 2:
                raise ValueError("Атрибут increasing_coef должен иметь значение в промежутке от 1 до 2 включительно")
            self.increasing_coef = increasing_coef

        def total_area(self) -> float:
            """
            Функция, которая считает общую площадь дуплекса со всеми входящими в него блоками, с учётом повышающего коэффициента

            Данный метод перегружается, поскольку меняется формула расчёта площади дома
            Считаем, что площадь дуплекса должна быть больше площади, посчитанной в базовом классе, в количество раз равное increasing_coef
            Дуплекс состоит из двух блоков, поэтому посчитанную площадь домножаем на 2

            :return: Площадь дуплекса
            """
            return self.increasing_coef * self.floor_area * self.number_of_floors * 2

        def __repr__(self) -> str:
            """
            Определяет поведение функции repr(), вызванной от экземпляра класса Duplex
            Перегружаем метод, поскольку в данном дочернем классе расширился конструктор базового класса
            Требуется дополнить информацию о добавленных атрибутах

            :return: f-string
            """
            return f"{self.__class__.__name__}(name_of_the_complex={self.name_of_the_complex!r}, floor_area={self.floor_area!r}, number_of_floors={self.number_of_floors!r}, increasing_coef={self.increasing_coef!r})"

    class Townhouse(House):
        """ Дочерний класс дома. """
        def __init__(self, name_of_the_complex: str, floor_area: float, number_of_floors: int, number_of_blocks: int):
            """
            Создание и подготовка к работе объекта "Таунхаус"

            :param name_of_the_complex: Название жилого комплекса
            :param floor_area: Площадь этажа
            :param number_of_floors: Количество этажей
            :param number_of_blocks: Количество блоков
            """
            super().__init__(name_of_the_complex, floor_area, number_of_floors)

            if not isinstance(number_of_blocks, int):
                raise TypeError("Атрибут number_of_blocks должен иметь тип int")
            if number_of_blocks < 1:
                raise ValueError("Атрибут number_of_blocks должен быть положительным числом и иметь значение больше или равное 1")
            self.number_of_blocks = number_of_blocks

        def total_area(self) -> float:
            """
            Функция, которая считает общую площадь таунхауса со всеми входящими в него блоками

            Данный метод перегружается, поскольку меняется формула расчёта площади дома
            Считаем плоащадь с учётом количества блоков, указанного в атрибуте number_of_blocks

            :return: Площадь таунхауса
            """
            return self.floor_area * self.number_of_floors * self.number_of_blocks

        def __repr__(self) -> str:
            """
            Определяет поведение функции repr(), вызванной от экземпляра класса Townhouse
            Перегружаем метод, поскольку в данном дочернем классе расширился конструктор базового класса
            Требуется дополнить информацию о добавленных атрибутах

            :return: f-string
            """
            return f"{self.__class__.__name__}(name_of_the_complex={self.name_of_the_complex!r}, floor_area={self.floor_area!r}, number_of_floors={self.number_of_floors!r}, number_of_blocks={self.number_of_blocks!r})"
    pass
#перенос строки