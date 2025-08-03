from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.mark.parametrize('length', [0, 1, 25, 39, 40, 41, 50])
    def test_add_new_book_name_length(self, length):
        name='a' * length
        collector=BooksCollector()
        collector.add_new_book(name)
        if 0 < length < 41:
            assert len(collector.books_genre) == 1
        else:
            assert len(collector.books_genre) == 0
        
    
    def test_set_book_genre_set_genre_horror(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.get_book_genre(name) == 'Ужасы'

    def test_set_book_genre_set_genre_random(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'RANDOM')
        assert collector.get_book_genre(name) == ''
   
    def test_set_book_genre_set_genre_to_missing_book(self):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre('Идиот', 'Ужасы')
        assert collector.get_book_genre(name) == ''
        assert not collector.books_genre.get('Идиот')

    def test_get_books_with_specific_genre_get_two_horror_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        books=collector.get_books_with_specific_genre('Ужасы')
        assert len(books) == 2 \
        and 'Гордость и предубеждение и зомби' in books \
        and 'Что делать, если ваш кот хочет вас убить' in books

    def test_get_books_genre_list_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        books=collector.get_books_genre()
        assert len(books) == 2 \
        and books.get('Гордость и предубеждение и зомби') == 'Ужасы' \
        and books.get('Идиот') == 'Мультфильмы'

    def test_get_books_for_children_list_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        books=collector.get_books_for_children()
        assert len(books) == 1 and 'Идиот' in books

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Идиот')
        books=collector.get_list_of_favorites_books()
        assert len(books) == 2 and 'Идиот' in books and 'Гордость и предубеждение и зомби' in books

    def test_add_book_in_favorites_add_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Идиот')
        collector.add_book_in_favorites('Идиот')
        books=collector.get_list_of_favorites_books()
        assert len(books) == 1 and 'Идиот' in books

    def test_add_book_in_favorites_add_missing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Идиот')
        books=collector.get_list_of_favorites_books()
        assert len(books) == 1 and 'Гордость и предубеждение и зомби' in books

    def test_delete_book_from_favorites_delete_one_of_two(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Идиот')
        collector.delete_book_from_favorites('Идиот')
        books=collector.get_list_of_favorites_books()
        assert len(books) == 1 and 'Гордость и предубеждение и зомби' in books
        