from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'username', 'email',
                    'bio', 'first_name', 'last_name',)


admin.site.register(User, UserAdmin)