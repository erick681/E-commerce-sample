from django.urls import path
from .views import *
app_name ='core'
urlpatterns = [
    path('',index, name = 'welcome'),
    path('login',user_login, name = 'login'),
    path('sign_up',sign_up,name='sign_up'),
    path('exit',logout_view,name='logout'),
    path('pass_change',pass_change,name ='pass_change'),
]