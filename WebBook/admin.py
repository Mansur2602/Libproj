from django.contrib import admin
from .models import Authors, Books
# Register your models here.
admin.register( [Authors, Books] )
