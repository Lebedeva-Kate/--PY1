class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги."""
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно иметь тип данных int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    # Ожидаем, что метод __str__ будет будет задействовать все атрибуты экземпляра данного класса.
    # В этом классе помимо атрибутов базового класса появляется атрибут pages.
    # Исходя из этого перегружаем метод __str__.
    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}."

    # Ожидаем, что метод __repr__ будет задействовать все атрибуты экземпляра класса.
    # В этом классе помимо атрибутов базового класса появляется атрибут pages.
    # Исходя из этого перегружаем метод __repr__.
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    """ Дочерний класс книги."""
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "Аудиокнига"

        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность аудиокниги
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна иметь тип данных float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть представлена положительным числом")
        self._duration = new_duration

    # Ожидаем, что метод __str__ будет задействовать все атрибуты экземпляра данного класса.
    # В этом классе помимо атрибутов базового класса появляется атрибут duration.
    # Исходя из этого перегружаем метод __str__.
    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}."

    # Ожидаем, что метод __repr__ будет задействовать все атрибуты экземпляра данного класса.
    # В этом классе помимо атрибутов базового класса появляется атрибут duration.
    # Исходя из этого перегружаем метод __repr__.
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
# перенос строки
