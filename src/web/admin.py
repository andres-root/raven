from django.contrib import admin
from web.models import Book, BookMedia, Author, Genre


admin.site.register(Book)
admin.site.register(BookMedia)
admin.site.register(Author)
admin.site.register(Genre)
