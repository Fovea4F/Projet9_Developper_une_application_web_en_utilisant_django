from django.contrib import admin
from review.models import Ticket
from review.models import Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'user', 'image', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user', 'headline', 'body', 'time_created')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
