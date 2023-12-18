from django import forms
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):

    class Meta:
        model = models.Ticket
        fields = ['user', 'title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.Form):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
