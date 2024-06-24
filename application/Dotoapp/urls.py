from django.urls import path 
from . import views


urlpatterns = [path(''  ,  views.view , name ="Home") , 
                path('/transaction', views.your_view, name='transaction'),

               ]