from django.contrib import admin
from .models import User

admin.site.site_header = 'Панель администратора'
admin.site.site_title = 'Управление проектом'
admin.site.index_title = 'Управление проектом'


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'username', 'email',
                    'bio', 'first_name', 'last_name',)

# зарегистрируйте здесь свои модели

admin.site.register(User, UserAdmin)