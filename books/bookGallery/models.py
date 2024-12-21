from django.db import models
from django.urls import reverse
from slugify import slugify
from django.contrib.auth.models import User

class Publisher(models.Model):
    phone = models.IntegerField(verbose_name="Телефон")
    name = models.CharField(max_length=255, verbose_name="Название издательства")

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publishersView', kwargs={'pub_id': self.pk})
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    dateBirth = models.DateField(verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authorsView', kwargs={'author_id': self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('genreView', kwargs={'genre_id': self.pk})

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    amount = models.IntegerField(null=True, verbose_name="Количество книг")
    price = models.IntegerField(verbose_name="Цена")
    cover = models.ImageField(upload_to="books/", verbose_name="Обложка")
    description = models.TextField(verbose_name="Описание")
    publication_year = models.DateField(verbose_name="Дата публикации")
    author = models.ManyToManyField(Author, verbose_name="Авторы")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Издатель")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name="Жанр")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Генерация slug из названия книги
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bookView', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def decrease_Amount(self):
        self.amount -= 1
        self.save()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

class Status(models.Model):
    status_name = models.CharField(max_length=255, verbose_name="Статус")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Order(models.Model):
    date = models.DateField(auto_now=True, verbose_name="Дата заказа")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Заказчик")
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1, verbose_name="Статус заказа")
    books = models.ManyToManyField(Book, verbose_name="Заказанные книги")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['user', 'status', 'date']

