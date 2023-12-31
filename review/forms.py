from django import forms
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):

    class Meta:
        model = models.Ticket
        fields = ['user', 'title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['user'].queryset = User.objects.filter(pk=user.pk)
            self.fields['user'].widget.attrs['readonly'] = 'readonly'


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class ReviewFormDual(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].required = False


class DeleteReviewForm(forms.Form):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class UserFollowsForm1(forms.Form):

    def __init__(self, *args, **kwargs):
        users = kwargs.pop('not_followed_users')
        super(UserFollowsForm1, self).__init__(*args, **kwargs)
        self.fields['follows'] = forms.ModelMultipleChoiceField(queryset=users, widget=forms.CheckboxSelectMultiple)


class FollowsUsersForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        filtered_queryset = kwargs.pop('filtered_queryset', None)
        super(FollowsUsersForm, self).__init__(*args, **kwargs)

    # 'queryset' used to dynamically filter du champ ModelChoiceField
        self.fields['follows'].queryset = filtered_queryset


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
