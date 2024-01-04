
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from review.models import Ticket, Review
from authentication.models import User
from .forms import TicketForm, ReviewForm, ReviewFormDual, DeleteTicketForm, DeleteReviewForm
from .forms import FollowsUsersForm, RatingForm


@login_required
def home(request):
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")  # most recent before
    tickets_and_review = []
    for ticket in tickets:
        review = ticket.review_set.first()
        if not review:
            review = ''
        tickets_and_review.append((ticket, review))
    context = {
        'tickets_and_review': tickets_and_review
        }
    return render(request, 'review/home.html', context)


@login_required
def post(request):
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")  # most recent before
    tickets_and_review = []
    for ticket in tickets:
        review = ticket.review_set.first()
        if not review:
            review = ''
        tickets_and_review.append((ticket, review))
    context = {
        'tickets_and_review': tickets_and_review
        }
    return render(request, 'review/post.html', context)


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'review/ticket_view.html', {'ticket': ticket})


@login_required
def ticket_create(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    context = {'ticket_form': ticket_form}
    return render(request, 'review/ticket_create.html', context=context)


@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('post')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }

    return render(request, 'review/ticket_edit.html', context)


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    delete_form = DeleteTicketForm()
    if request.method == 'POST':
        if 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('post')
    context = {
        'delete_form': delete_form,
        }
    return render(request, 'review/ticket_delete.html', context=context)


@login_required
def review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review/review_view.html', {'review': review})


@login_required
def review_edit(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    edit_form = ReviewForm(instance=review)
    delete_form = DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'review/review_edit.html', context=context)


@login_required
def review_create(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form = ReviewForm(request.POST)
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
        else:
            review_form = ReviewForm()
    else:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        review_form = ReviewForm(request.POST)
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'review/review_create.html', context=context)


@login_required
def review_ticket_create(request):
    ticket_form = TicketForm(request.user)
    review_form = ReviewFormDual(request.user)

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewFormDual(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            if review_form.is_valid():
                review = review_form.save(commit=False)
                if (review.rating):
                    review.user = request.user
                    review.ticket = ticket
                    review.save()
        return redirect('home')
    else:
        ticket_form = TicketForm(user=request.user)
        # ticket_form.fields['user'].widget.attrs['disabled'] = 'disabled'
        review_form = ReviewFormDual(initial={'rating': None})

    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/review_ticket_create.html', context=context)


@login_required
def review_ticket_edit(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = get_object_or_404(Review, ticket_id=ticket.id)
    # ticket_form = TicketForm(instance=ticket)
    review_form = ReviewForm(instance=Review)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('post')
        else:
            print(review_form.errors)
            ticket = get_object_or_404(Ticket, id=ticket_id)
            review = get_object_or_404(Review, ticket_id=ticket.id)
            review_form = ReviewForm(instance=review)
            rating_form = RatingForm(initial={'rating': review.rating})
    else:
        review_form = ReviewForm(instance=review)
        rating_form = RatingForm(initial={'rating': review.rating})

    context = {
        'review_form': review_form,
        'ticket': ticket,
        'rating_form': rating_form,
        'loop_times': range(0, 6),
        }
    return render(request, 'review/review_ticket_edit.html', context=context)


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    delete_review_form = DeleteReviewForm()
    if request.method == 'POST':
        if 'delete_review' in request.POST:
            delete_review_form = DeleteReviewForm(request.POST)
            if delete_review_form.is_valid():
                review.delete()
                return redirect('post')
    context = {
        'delete_review_form': delete_review_form,
        }
    return render(request, 'review/review_delete.html', context=context)


@login_required
def follow_users_ori(request):

    if request.method == 'POST':
        form = FollowsUsersForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = FollowsUsersForm(request.user)
        print('toto')

    context = {'form': form}

    return render(request, 'review/follow_users.html', context)


@login_required
def follow_users2(request):
    form = FollowsUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowsUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'review/follow_users.html', context={'form': form})


@login_required
def follow_users_test(request):

    filtered_users = User.objects.exclude(pk=request.user.pk).exclude(is_staff=True)

    form = FollowsUsersForm(instance=request.user, filtered_queryset=filtered_users)
    if request.method == 'POST':
        form = FollowsUsersForm(request.POST, instance=request.user, filtered_queryset=filtered_users)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'review/follow_users_form.html', context={'form': form})


@login_required
def follow_users(request):

    filtered_users = User.objects.exclude(pk=request.user.pk).exclude(is_staff=True)

    form = FollowsUsersForm(instance=request.user, filtered_queryset=filtered_users)
    if request.method == 'POST':
        form = FollowsUsersForm(request.POST, instance=request.user, filtered_queryset=filtered_users)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'review/follow_users_form.html', context={'form': form})
