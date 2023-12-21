from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Ticket, Review, UserFollows
from authentication.models import User
from .forms import TicketForm, ReviewForm, DeleteTicketForm, DeleteReviewForm, UserFollowsForm


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
    edit_form = TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('post')
    context = {
        'edit_form': edit_form,
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
def review_ticket_edit1(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = ticket.review_set.first()
    if request.method == 'POST':
        ticket_form = TicketForm(instance=ticket)
        review_form = ReviewForm(instance=review)
        if ticket_form.is_valid():
            ticket_form.save()

            if review_form.is_valid():
                review_form.save()
            return redirect('post')
    else:
        ticket_form = TicketForm(instance=ticket)
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
        }
    return render(request, 'review/review_ticket_edit.html', context=context)


@login_required
def review_ticket_create(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/review_ticket_create.html', context=context)


@login_required
def review_ticket_edit(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = ticket.review_set.first()
    edit_review_form = ReviewForm(instance=review)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_ok = edit_review_form.save(commit=False)
            review_ok.save()
            return redirect('post')
    context = {
        'ticket': ticket,
        'edit_review_form': edit_review_form,
        }
    return render(request, 'review/review_ticket_edit.html', context=context)


@login_required
def review_ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    delete_ticket_form = DeleteTicketForm()
    if request.method == 'POST':
        delete_ticket_form = DeleteTicketForm(request.POST)
        ticket.delete()
        return redirect('post')
    context = {
        'delete_ticket_form': delete_ticket_form,
        }
    return render(request, 'review/review_ticket_delete.html', context=context)


@login_required
def follow_users1(request):

    user_id = request.user
    follow_form = UserFollows.objects.filter().exclude(user=user_id)
    '''follow_form = UserFollows.objects.filter(
                        user=request.user).exclude(
                        user=UserFollows.user,
                        followed_user=UserFollows.followed_user
                        )'''
    if request.method == 'POST':
        follow_form = UserFollowsForm(request.POST, user_id)
        if follow_form.is_valid():
            follow_form.save()
            return redirect('home')
    context = {'follow_form': follow_form}
    return render(request, 'review/follow_user.html', context)


@login_required
def follow_users(request):

    not_followed_users = User.objects.filter(
            Q(follows__in=request.user.follows.all())
    )

    if request.method == 'POST':
        form = UserFollowsForm(request.POST, queryset=not_followed_users)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = UserFollowsForm(request.user, queryset=not_followed_users)
        print('toto')

    context = {'form': form}

    return render(request, 'review/follow_user.html', context)
