from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.about,name = 'abuot',kwargs = {'name':'Ann','work':'teacher'}),
    # path(r'^about/[0-9]{4}', views.about, name='abuot'),
    path('contacts', views.about, name='contacts'),



]
