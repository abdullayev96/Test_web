from django.urls import path
from .views import *



urlpatterns=[
    path('new/', home, name="home_page"),
    path('new/<int:pk>/',BookDetailView.as_view(), name="detail"),
    path('contact/', contact, name="contact"),

    
    #path('new/<int:pk>/', BookDetailView.as_view(), name='detail'),
    # path('author/', author_list, name="author_list"),
    # path('author/<int:author_id>/', author_details, name="author_details"),
    # path('genre/', genre_list, name="genre_list"),
    # path('genre/<int:genre_id>/', genre_details, name="genre_details"),
    # path('book/', book_list, name="book_list"),
    # path('book/<int:book_id>/', book_details, name="book_details")
]
