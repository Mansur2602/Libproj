# data generator for models
from .models import Authors, Books
from random  import randint, choice

list_authors = [
    'Пушкин А.С.', "Лермонтов М.Ю.", "Абай К.",
    "Шекли", "Шекспир У.", "Байрон", "Шоу Б.",
    "Лем С", "Достоевский Ф.М." ]
list_contry = ["Россия", "Казахстан", "Америка", "Англия", "Францичя"]

# ф-ция генерации случайной строки
def rand_str( min_length = 4, max_length = 10 ):
    length = randint( min_length, max_length )
    str_res = chr( randint( ord('A'), ord('Z') ) )
    for i in range( length-1 ):
        #str_res += randint( 97, 122 )
        str_res += chr( randint( ord('a'), ord('z') ) )
    return str_res
        
   


# сгенерирова одного автора случайным образом и поместить в таблицу авторов
def gen_author():
    # 1 вариант заполнения одной записи в таблицу Authors
    # a = Authors()
    # a.fio = choice( list_authors )
    # a.birth_year = randint( 1000, 2024 )
    # a.country = choice( list_contry )
    # a.save()
    # 2 вариант заполнения одной записи в таблицу Authors
    # a = Authors( fio = choice( list_authors ),
    #              birth_year = randint( 1000, 2024 ),
    #              country = choice(list_contry) )
    # a.save()
    # 3 вариант заполнения одной записи в таблицу Authors
    Authors( fio = choice( list_authors ),
             birth_year = randint( 1000, 1990 ),
             country = choice(list_contry) ).save()

list_genre = [ "Роман", "Новелла", "Повесть", "Фантастика",
               "Очерк", "Детектив" ] 
# сгенерировать одну запись для книги
def gen_book():
    # SELECT id, birth_year FROM Authors
    #authors_all = Authors.objects.values_list('id', 'birth_year').all()
    # authors_all_id = [ (1,1900), (2,1762), (3,1842) ]

    # SELECT id FROM Authors
    authors_all_id = list(Authors.objects.all().values_list('id'))
    # authors_all_id = [ (1,), (2,), (3,) ]
    sel_author_id = choice(authors_all_id)[0]
    # извлекаем из БД автора с id = sel_author_id
    sel_auth = Authors.objects.get( pk=sel_author_id )
    b = Books()
    # создать случайное название для книги из двух случ. слов
    b.name = rand_str(5, 12) + ' ' + rand_str(7, 20)
    b.year  = sel_auth.birth_year + randint(13, 60)
    b.genre = choice( list_genre )
    b.id_author = sel_auth  # b.id_author = sel_auth.id
    b.save()
