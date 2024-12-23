# Generated by Django 5.1.4 on 2024-12-19 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookGallery', '0003_status_alter_author_options_alter_book_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
