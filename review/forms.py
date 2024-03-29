from django import forms
from django.contrib.auth import get_user_model
from . import models
from review.models import UserFollows

User = get_user_model()


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    # edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewFormDual(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].required = False


class FollowsUsersForm(forms.ModelForm):

    class Meta:
        model = UserFollows
        fields = ['followed_user',]
        labels = {'followed_user': 'Abonné'}

    def __init__(self, *args, **kwargs):
        filtered_queryset = kwargs.pop('filtered_queryset', None)
        super(FollowsUsersForm, self).__init__(*args, **kwargs)

        # 'queryset' used to dynamically filter du champ ModelChoiceField
        self.fields['followed_user'].queryset = filtered_queryset


class RatingForm(forms.Form):
    RATING = (
        (0, ' - 0'),
        (1, ' - 1'),
        (2, ' - 2'),
        (3, ' - 3'),
        (4, ' - 4'),
        (5, ' - 5'),
    )

    rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect(), required=True, label='Note :')
