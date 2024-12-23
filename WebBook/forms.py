from django import forms
from .models import Authors, Books

class FormNewAuthor(forms.ModelForm):

    class Meta:
        model = Authors
        fields = ['fio', 'birth_year', 'country', 'photo']


class FormNewBook(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['name', 'genre', 'year', 'id_author', 'cover']


