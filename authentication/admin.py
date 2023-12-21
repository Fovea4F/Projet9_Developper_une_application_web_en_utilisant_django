from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'is_active', 'date_joined', 'is_superuser', 'last_login')


admin.site.register(User, UserAdmin)       # nous modifions cette ligne, en ajoutant un deuxième argument