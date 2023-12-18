from django.contrib import admin
from authentication.models import User
from authentication.models import UserFollows


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'is_active', 'date_joined', 'is_superuser', 'last_login')


class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'followed_user')


admin.site.register(User, UserAdmin)       # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(UserFollows, UserFollowAdmin)