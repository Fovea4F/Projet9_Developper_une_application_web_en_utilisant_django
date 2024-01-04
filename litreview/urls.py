from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import authentication.views
import review.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name='login'),
    path("logout", authentication.views.logout_page, name='logout'),
    path("signup/", authentication.views.signup_page, name='signup'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'), name='password_change'),
    path('change-password-done', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'), name='password_change_done'),

    path("home/", review.views.home, name='home'),
    path("post/", review.views.post, name='post'),
    path('ticket/create', review.views.ticket_create, name='ticket_create'),
    path('ticket/<int:ticket_id>/edit/', review.views.ticket_edit, name='ticket_edit'),
    path('ticket/<int:ticket_id>/delete/', review.views.ticket_delete, name='ticket_delete'),
    path('review/create', review.views.review_ticket_create, name='review_ticket_create'),
    path('review/<int:ticket_id>/create', review.views.review_create, name='review_create'),
    path('review/<int:ticket_id>/edit/', review.views.review_ticket_edit, name='review_ticket_edit'),
    path('review/<int:review_id>/delete/', review.views.review_delete, name='review_delete'),
    path('review/follows', review.views.follow_users, name='follow_users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
