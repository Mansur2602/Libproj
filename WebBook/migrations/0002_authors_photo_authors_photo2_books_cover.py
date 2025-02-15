# Generated by Django 5.1.3 on 2024-12-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='images', verbose_name='Фотография автора'),
        ),
        migrations.AddField(
            model_name='authors',
            name='photo2',
            field=models.BinaryField(default=None, editable=True, null=True, verbose_name='Фотография автора 2'),
        ),
        migrations.AddField(
            model_name='books',
            name='cover',
            field=models.ImageField(default=None, null=True, upload_to='images', verbose_name='Обложка книги'),
        ),
    ]
