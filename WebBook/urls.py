from django.urls import path
from .views import view_gen_data, view_books, view_image, get_images, new_author, view_author, list_authors, new_book, view_book

urlpatterns = [
    path( '',            view_books,    name='home' ),
    path( 'gen/',        view_gen_data, name='view_gen_data' ),
    path( 'books/',      view_books,    name='view_books' ),
    path( 'view_image/', view_image,    name='view_image' ),
    path( 'images/',     get_images,    name='images' ),
    path('new_author/',   new_author,      name='new_author' ),
    path('view_auth/<int:id_author>', view_author, name='view_author'),
    path('list_authors/', list_authors, name='list_author'),
    path('new_book/', new_book, name='new_book' ),
    path('view_book/<int:id>/', view_book, name='view_book'),
]

