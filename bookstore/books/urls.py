from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('authors',views.authors,name='authors'),
    path('books',views.books,name='books'),
    path('authorDetails/<int:authorId>',views.authorDetails,name='authorDetails')

]