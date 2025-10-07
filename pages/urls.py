from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('gallery/', views.gallery, name='gallery'),
    # path('posts/', views.post_list, name='post_list'),
    path('admin/', views.admin, name='admin'),
    # path('post/new/', views.post_create, name='post_create'),
    # path('post/<int:pk>/view/', views.post_view, name='post_view'),
    # path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('categories/', views.category_list, name='category_list'),
]