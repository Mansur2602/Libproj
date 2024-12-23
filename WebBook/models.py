from django.db import models

# Create your models here.
'''
Authors - Авторы: ФИО, год рождения, страна проживания;
Books   - Книги:  название книги, жанр, год написания, id-автора;
'''
class Authors( models.Model ):
    # id = models.BigAutoField(primary_key=True)
    fio = models.CharField( max_length=100, verbose_name='ФИО автора', null = False )
    birth_year = models.IntegerField( verbose_name='Год рождения' )
    country    = models.CharField( max_length= 50, verbose_name='Страна проживания' )
    photo = models.ImageField(upload_to = 'images', verbose_name='Фотография автора', null = True, default = None)
    photo2 = models.BinaryField(editable=True, verbose_name= 'Фотография автора 2', null = True, default = None )

class Books( models.Model ):
    # id = models.BigAutoField(primary_key=True)
    name  = models.CharField( max_length=200, verbose_name='Название книги' )
    genre = models.CharField( max_length=20, verbose_name='Жанр книги' )
    year  = models.IntegerField( verbose_name='Год написания' )
    id_author = models.ForeignKey( Authors, on_delete=models.CASCADE, verbose_name='Автор книги' )
    cover = models.ImageField(upload_to = 'images', verbose_name='Обложка книги', null = True, default = None)

