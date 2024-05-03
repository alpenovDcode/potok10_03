from books.book import Book
from books.catalog import Library
from users.review import Review
from users.review_manager import ReviewManager

# Создание книг и отзывов
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")

review1 = Review(book1, 5, "Amazing book!")
review2 = Review(book2, 4, "A must-read.")

# Управление библиотекой книг и отзывами
library = Library()
library.add_book(book1)
library.add_book(book2)

review_manager = ReviewManager()
review_manager.add_review(review1)
review_manager.add_review(review2)

# Вывод информации о книгах и отзывах
print("Books in Library:")
library.display_books()

print("\nReviews:")
review_manager.display_reviews()
