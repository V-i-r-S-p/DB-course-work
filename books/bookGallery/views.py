import datetime

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *

def main(request):
    return render(request, 'bookGallery/base.html')

def shopView(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    #paginator = Paginator(books, 50)

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    context = {
        'title' : 'Книги',
        'books' : books,
        'genres': genres,
        'current_genre': 0
    }
    return render(request, 'bookGallery/shopView.html', context=context)

def bookView(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'bookGallery/bookView.html', {'book' : book})

def login(request):
    return render(request, 'bookGallery/login.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'bookGallery/register.html'
    success_url = reverse_lazy('login')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'bookGallery/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def show_by_genre(request, genre_id):
    books = Book.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    # paginator = Paginator(books, 50)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'title': f'Книги по жанру: {Genre.objects.get(pk=genre_id).name}',
        'books': books,
        'genres': genres,
        'current_genre': genre_id
    }

    return render(request, 'bookGallery/shopView.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def authorView(request, author_id=0):
    books = Book.objects.filter(author=author_id)
    authors = Author.objects.all()
    genres = Genre.objects.all()
    # paginator = Paginator(books, 50)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    BookContext = {
        'title': f'Книги по Автору: {Author.objects.get(pk=author_id).name}' if author_id >=1 else '',
        'books': books,
        'genres': genres,
        'current_genre': 0
    }

    AuthorContext = {
        'title': "Авторы книг",
        'authors': authors
    }

    if author_id == 0:
        return  render(request, 'bookGallery/authorView.html', context=AuthorContext)
    else:
        return render(request, 'bookGallery/shopView.html', context=BookContext)

def publisherView(request, pub_id=0):
    books = Book.objects.filter(author=pub_id)
    publishers = Publisher.objects.all()
    genres = Genre.objects.all()
    # paginator = Paginator(books, 50)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    BookContext = {
        'title': f'Книги по Издательству: {Publisher.objects.get(pk=pub_id).name}' if pub_id >= 1 else '',
        'books': books,
        'genres': genres,
        'current_genre': 0
    }

    PublisherContext = {
        'title': "Издатели книг",
        'publishers': publishers
    }

    if pub_id == 0:
        return render(request, 'bookGallery/publishersView.html', context=PublisherContext)
    else:
        return render(request, 'bookGallery/shopView.html', context=BookContext)


def orders(request):
    orders = Order.objects.filter(user=request.user)
    status = Status.objects.get(status_name="Корзина")

    try:
        busket = Order.objects.get(user=request.user, status=status.pk)
        busket_id = busket.pk
    except Exception as e:
        busket_id = -1

    context = {
        'title': f'Заказы',
        'orders': orders,
        'busket_id': busket_id
    }

    return render(request, 'bookGallery/ordersView.html', context=context)

def profile(request):
    return HttpResponse('WIP')

def addOrder(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        # Добавляем новый экземпляр модели Order
        book_id = request.POST.get("book_id", 1)
        previous_page = request.POST.get('next', '')

        book = Book.objects.get(pk=book_id)



        status = Status.objects.get(status_name="Корзина")

        order = None
        try:
            order = Order.objects.get(user=request.user, status=status.pk)

        except Exception as e:
            order = Order.objects.create(date=datetime.date, user=request.user, status=status)

        book.decrease_Amount()
        order.books.add(book)
        order.save()


        # Проверяем значение redirect
        if request.POST.get("redirect") == "true":
            return redirect("orders")  # Перенаправление на список заказов

        return redirect(previous_page if previous_page else 'home')

    return redirect('home')