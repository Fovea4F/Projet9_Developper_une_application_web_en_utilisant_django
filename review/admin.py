from django.contrib import admin
from review.models import Ticket
from review.models import Review
# from review.models import UserFollows


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'user', 'image', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user', 'headline', 'body', 'time_created')


class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'followed_user')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
# admin.site.register(UserFollows, UserFollowAdmin)
