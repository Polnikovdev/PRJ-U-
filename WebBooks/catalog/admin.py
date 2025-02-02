from django.contrib import admin

# Register your models here.
from.models import Author, Book, Genre, Language, Status, BookInstance
#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", "date_of_birth", "date_of_death"]

admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)

@admin.register(Book)
@admin.register(BookInstance)

#class BookInstanceInline(admin.TabularInline):
#    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    #list_display = ("title", "genre", "language", "display_author")
    #list_filter = ("genre", "author")
    #list_display = (display_author.short_description)
    
    #inlines = [BookInstanceInline]
    
    pass

class BookInstanceAdmin(admin.ModelAdmin):
    #pass
    #list_filter = ("book", "status")
    #fieldsets = (("Экземпляр книги", {'fields': ('book', 'imprint', 'inv_nom')}), ("Статус и окончание его действия", {"fields": ("status", "due_back")}),)
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    
BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')




admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)


