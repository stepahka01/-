from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='home',kwargs = {'name':'Рудько Анастасия Антоновна','age':'17','interes':'Нету'}),
    path('about',views.about,name = 'about',kwargs = {'city':'Чебоксары','eval':'хорошя'}),
    path('contacts', views.contacts, name='contacts'),

]
