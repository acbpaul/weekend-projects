from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("", views.index, name="index"),
    path('books/', views.book_list, name='book_list')
]