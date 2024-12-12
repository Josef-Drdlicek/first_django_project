from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('add-data/', views.add_data, name='add_data'),
    path('data-table/', views.data_table, name='data_table'),
    path('about/', views.about, name='about'),
]
