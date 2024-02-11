from django.urls import path
from . import views
from django.contrib.auth import views as authViews
urlpatterns = [
 path('', views.index, name='index'),
 path('about', views.about, name='about'),
 path('pat', views.pat),
 path('goods', views.goods, name='goods'),
 path('login/', views.login_view, name='login'),
 path('register/', views.register, name='register'),
 path('logout/', authViews.LogoutView.as_view(next_page=''), name='logout'),
 path('create', views.create, name='create'),
 path('delete/<int:pk>/', views.delete, name='delete'),
]
