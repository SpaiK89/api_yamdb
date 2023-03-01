from django.contrib import admin
from .models import User, Comment, Review

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

# зарегистрируйте здесь свои модели

admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)