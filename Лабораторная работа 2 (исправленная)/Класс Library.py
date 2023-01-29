from pydantic import BaseModel, conint

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book(BaseModel):
    id_: int
    name: str
    pages: int = conint(gt=0)
    """
    Создание и подготовка к работе объекта "Книга"

    :param id_: ID книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    """
    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library(BaseModel):
    books: list = []
    """
    Создание и подготовка к работе объекта "Библиотека"

    :param books: Книги, содержащиеся в библиотеке
    """
    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку

        :return: Идентификатор новой книги
        """
        if self.books == []:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id: int):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param id: ID книги

        :return: Индекс книги в списке
        """
        if not isinstance(id, int):
            raise TypeError("ID книги должно иметь тип данных int")
        if id <= 0:
            raise ValueError("ID книги должно быть положительным числом")

        for index, book in enumerate(self.books):
            if book.id_ == id:
                return index
            elif index < self.books[-1].id_ - 1:
                index += 1
            else:
                raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
# перенос строки
