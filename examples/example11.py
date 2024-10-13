def book_list(books, func):
    for book in books:
        print(func(book))

books = ['Введение в психоанализ','Сапиенс - краткая история человечества','Рагнарёк']

book_list(books, lambda book: book.upper() + ' - прочитано')



