# Generated by Django 3.0.3 on 2020-03-14 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_fiyat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='fiyat',
            new_name='price',
        ),
    ]
