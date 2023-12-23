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


class UserFollowsForm2(forms.Form):

    def __init__(self, *args, **kwargs):
        users = kwargs.pop('not_followed_users')
        super(UserFollowsForm2, self).__init__(*args, **kwargs)
        self.fields['follows'] = forms.ModelMultipleChoiceField(queryset=users, widget=forms.CheckboxSelectMultiple)


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']


class RatingForm(forms.Form):
    RATING = (
        (0, ' - 0'),
        (1, ' - 1'),
        (2, ' - 2'),
        (3, ' - 3'),
        (4, ' - 4'),
        (5, ' - 5'),
    )

    rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True)
