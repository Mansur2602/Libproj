from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, FileResponse, HttpResponseNotFound
from django.core.paginator import Paginator, Page
from .data_gen import gen_book, gen_author
from .models import Authors, Books
from django.conf import settings
from .forms import FormNewAuthor, FormNewBook
from os.path import exists


# Create your views here.
def view_gen_data( req : HttpRequest ) -> HttpResponse:
    # генерируем случ. 10 авторов
    for i in range(10):
        gen_author()
    # генерируем случ. 20 книг
    for i in range(20):
        gen_book()
    return HttpResponse( 'Сгенерированы данные для авторов и книг' )

def view_books( req : HttpRequest ) -> HttpResponse:
    # SELECT * FROM Books
    books = Books.objects.all()
    paging = Paginator( books, per_page=10, orphans=0, allow_empty_first_page=True )
    not_found =  str(settings.MEDIA_URL) + 'images/not_found.jpg'
    # обработка GET-запроса
    num_page = 1  # номер текущей страницы списка книг
    if 'page' in req.GET:
        num_page = req.GET['page']    
    page = paging.page( num_page )
    return render( req, 'books.html',
                   { 'page' : page, 'title' : f'Список книг - {num_page} страница', 'not_found': not_found } )
    

def view_image( req : HttpRequest ) -> HttpResponse:
    img_name  = "not_found.jpg"
    base_path = str(settings.BASE_DIR)
    print('BASE_DIR = ', base_path)
    # http://myWebServer.com/images/?img=Pushkin.jpg
    if 'img' in req.GET:
        img_name = req.GET['img']
        # C:\proj\webBook\images\Pushkin.jpg
        img_full_path = base_path + r'\WebBook\images' + '\\' + img_name
        if not exists( img_full_path ):
            img_name  = "not_found.jpg"
    img_full_path = base_path + r'\WebBook\images' + '\\' + img_name
    return FileResponse( open(img_full_path, 'rb'), as_attachment=False )

def get_images( req ):
    return render( req, 'images.html' )


def new_author(req : HttpRequest) -> HttpResponse:
    status = None
    form = FormNewAuthor()
    if req.method == 'POST':
        form = FormNewAuthor(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            status = 'Данные сохранены'
            form = FormNewAuthor()
        else:
            status = 'Данные не сохранены'
    return render(req, 'new_author.html', { 'form': form, 'status': status, 'title': 'Ввод данных для авторов'  })

def view_author(req : HttpRequest, id_author: int) -> HttpResponse:
    # author = Authors.objects.get(pk = id_author)
    author = Authors.objects.filter(pk = id_author).first()
    if author is not None:
        if author.photo:
            photo_path =  str(settings.MEDIA_ROOT) + str(author.photo)
            if not exists(photo_path):
                author.photo = 'images/not_found.jpg'
        else:
            author.photo = 'images/not_found.jpg'

        return render(req, 'author.html', { 'data': author, 'title': f'Информация об авторе: {author.fio}' } )

    else:
        return HttpResponseNotFound(content = f'Автора с id = {id_author} нет!')


def list_authors(req : HttpRequest,) -> HttpResponse:

    list_authors = Authors.objects.all()
    paging = Paginator( list_authors, per_page=10, orphans=0, allow_empty_first_page=True )
    not_found =  str(settings.MEDIA_URL) + 'images/not_found.jpg'
    num_page = 1  
    if 'page' in req.GET:
                num_page = req.GET['page']    
        
    page = paging.page( num_page )
    return render( req, 'authors_list.html', { 'page' : page, 'title' : f'Список авторов - {num_page} страница', 'not_found': not_found} )

def new_book(req : HttpRequest) -> HttpResponse:
    status = None
    form = FormNewBook()
    if req.method == 'POST':
        form = FormNewBook(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            status = 'Данные сохранены'
            form = FormNewBook()
        else:
            status = 'Данные не сохранены'
    return render(req, 'new_book.html', { 'form': form, 'status': status, 'title': 'Ввод данных для книги'  })


def view_book(req : HttpRequest, id: int) -> HttpResponse:
 
    book = Books.objects.filter(pk = id).first()
    if book is not None:
        if book.cover:
            photo_path =  str(settings.MEDIA_ROOT) + str(book.cover)
            if not exists(photo_path):
                book.cover = 'images/not_found.jpg'
        else:
            book.cover= 'images/not_found.jpg'

        return render(req, 'book.html', { 'book': book, 'title': f'Информация об книге: {book.name}' } )

    else:
        return HttpResponseNotFound(content = f'Книги с id = {id} нет!')


