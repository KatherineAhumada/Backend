
from django.urls import path
from . import views


urlpatterns = [
path('pagina1', views.index, name='pagina1'),  
path('pagina2', views.index, name='pagina2'),  
path('pagina3', views.index, name='pagina3'),  
]
