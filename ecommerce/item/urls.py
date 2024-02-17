from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import * 

app_name = 'item'
urlpatterns = [
    path('',items,name='items'),
    path('<int:pk>',details,name = 'details'),
    path('new',new,name='new'),
    path('<int:pk>/delete',delete,name='delete'),
    path('<int:pk>/edit',edit,name='edit')
]