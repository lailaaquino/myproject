app_name = 'edu'
from django.urls import include, path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.list_livros, name='list_livros'),
    path('editoras/', views.list_editoras, name='list_editoras'),
    path('autores/', views.list_autores, name='list_autores'),

    path('livro/create/', views.livro_create, name='livro_create'),
    path('editora/create/', views.editora_create, name='editora_create'),
    path('autor/create/', views.autor_create, name='autor_create'),

    path('livro/edit/<int:id>/', views.edit_livros, name='edit_livros'),
    path('editora/edit/<int:id>/', views.edit_editoras, name='edit_editoras'),
    path('autor/edit/<int:id>/', views.edit_autores, name='edit_autores'),

    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    
    path('api/', include('edu.api_urls')),
]