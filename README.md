# qa_python
1. test_add_new_book_add_two_books #Проверяем добавление двух книг методом add_new_book()

2. test_add_new_book_name_length #Прверяем для метода add_new_book() граничные значения на количество символов в назании добавляемой книги.

3. test_set_book_genre_set_genre_horror #Проверяем установку жанра Ужасы методом set_book_genre()

4. test_set_book_genre_set_genre_random #Проверяем, что не устанавливается несуществующий жанр методом set_book_genre()

5. test_set_book_genre_set_genre_to_missing_book #Проверяем, что не устанавливается жанр на несуществующую книгу методом set_book_genre()

6. test_get_books_with_specific_genre_get_two_horror_books #Проверяем, что выводятся обе книги жанра Ужасы методом get_books_with_specific_genre()

7. test_get_books_genre_list_books #Проверяет, что выбираются все добавленные книги и их жанры методом get_books_genre()

8. test_get_books_for_children_list_books #Проверяем, что выбираются книги, которые подходят детям методом get_books_for_children()

9. test_add_book_in_favorites_add_two_books #Проверяем, что в избранное добавляются 2 разные существующие книги методом add_book_in_favorites()

10. test_add_book_in_favorites_add_book_twice #Проверяем, что в избранное не добавляе ранее добавленная книга методом add_book_in_favorites()

11. test_add_book_in_favorites_add_missing_book #Проверяем, что в избранное не добавляется несуществующая книга методом add_book_in_favorites()

test_delete_book_from_favorites_delete_one_of_two # Проверяем, что удаляется одна из двух добавленных в избранное книг методом delete_book_from_favorites()