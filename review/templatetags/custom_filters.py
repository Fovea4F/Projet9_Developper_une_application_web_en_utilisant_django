from django import template

register = template.Library()


@register.filter
def convert_to_stars_filter(rating):  # give 2 args : rating given, max_rating as maximum possible value

    max_rating = 5
    # args quality validation : 2 ints, with 0<rating<= max_rating
    if not (isinstance(rating, int) and isinstance(max_rating, int)):
        raise TypeError("Not valid arguments to convert to stars")
    elif not (0 <= rating <= max_rating):
        raise ValueError("Given values not compatibles with stars converter function")
    else:
        rating = int(rating)
        full_stars = '★' * rating  # Utilisation du caractère étoile pleine
        empty_stars = '☆' * (max_rating - rating)  # Utilisation du caractère étoile vide
        return f'{full_stars}{empty_stars}'


@register.simple_tag
def notation_boutons(max_value):

    boutons = ''
    for i in range(1, max_value):
        boutons += '<label><input type="radio" value="{i}">{i}</label>'
    return boutons
