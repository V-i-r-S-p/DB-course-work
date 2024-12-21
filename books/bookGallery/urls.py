from django.urls import path

from .views import *

urlpatterns = [
    path('', shopView, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('authors/', authorView, name="authors"),
    path('authors/<int:author_id>/', authorView, name="authorsView"),
    path('publishers/', publisherView, name="publishers"),
    path('publishers/<int:pub_id>/', publisherView, name="publishersView"),
    path('Genres/<int:genre_id>/', show_by_genre, name="genreView"),
    path('profile/', profile, name="profile"),
    path('orders/', orders, name="orders"),
    path("addOrder/", addOrder, name="addOrder"),

    path('<slug:slug>/', bookView, name='bookView'),
]