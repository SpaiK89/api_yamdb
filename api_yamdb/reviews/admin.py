from django.contrib import admin
from .models import User, Comment, Review, Title, Genre, Category

admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Управление проектом'
admin.site.index_title = 'Управление проектом'

VALUE_DISPLAY = '--Пусто--'


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'username', 'email',
                    'bio', 'first_name', 'last_name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'score', 'pub_date',)
    search_fields = ('author', 'title', 'text',)
    list_filter = ('score', 'text',)
    list_editable = ('author', 'title', 'text', 'score',)
    empty_value_display = VALUE_DISPLAY


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'review', 'text', 'pub_date',)
    search_fields = ('author', 'text', 'pub_date',)
    list_filter = ('author',)
    list_editable = ('author', 'review', 'text',)
    empty_value_display = VALUE_DISPLAY


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('year', 'genre', 'category',)


admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
