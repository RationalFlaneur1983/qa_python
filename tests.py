import pytest
from main import BooksCollector

class TestBooksCollector:

@pytest.fixture
def collector(self):
    return BooksCollector()

# Тест для add_new_book
    def test_add_new_book_add_two_books(self):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_name_over_40(self):
        collector.add_new_book("A" * 41)
        assert "A" * 41 not in collector.books_genre

# Тест для set_book_genre
    def test_set_book_genre_success(self):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Гордость, и предубеждение, и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость, и предубеждение, и зомби') == 'Фантастика'

    def test_set_book_genre_book_not_exist(self):
        collector.set_book_genre('Нет такой книги', 'Фантастика')
        assert collector.get_book_genre('Нет такой книги') is None

 # Тест для get_book_genre
    def test_get_book_genre_existing(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Гордость, и предубеждение, и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость, и предубеждение, и зомби') == 'Фантастика'

    def test_get_book_genre_not_exist(self, collector):
        assert collector.get_book_genre('Нет такой книги') is None

# Тест для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Гордость, и предубеждение, и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_with_specific_genre_no_books(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

# Тест для get_books_genre
    def test_get_books_genre(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Гордость, и предубеждение, и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость, и предубеждение, и зомби': 'Фантастика'}

# Тест для get_books_for_children
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Гордость, и предубеждение, и зомби', 'Фантастика')
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость, и предубеждение, и зомби']

# Тест для add_book_in_favorites
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.add_book_in_favorites('Гордость, и предубеждение, и зомби')
        assert 'Гордость, и предубеждение, и зомби' in collector.favorites

# Тест для delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.add_book_in_favorites('Гордость, и предубеждение, и зомби')
        collector.delete_book_from_favorites('Гордость, и предубеждение, и зомби')
        assert 'Гордость, и предубеждение, и зомби' not in collector.favorites

# Тест для get_list_of_favorites_books
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гордость, и предубеждение, и зомби')
        collector.add_book_in_favorites('Гордость, и предубеждение, и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость, и предубеждение, и зомби']
