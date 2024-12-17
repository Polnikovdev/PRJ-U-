from django.contrib import admin

# Register your models here.
from.models import Author, Book, Genre, Language, Status, BookInstance
#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")

admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)

@admin.register(Book)
@admin.register(BookInstance)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "language", "display_author")
    list_filter = ("genre", "author")
    #list_display = (display_author.short_description)
    #pass

class BookInstanceAdmin(admin.ModelAdmin):
    #pass
    list_filter = ("book", "status")



admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)


