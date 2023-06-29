from django.urls import path
from . import views
urlpatterns =[
    path('',views.recipient,name='recipient'),
    path('chathome/<str:username>',views.chatHome,name='chathome'),
    path('Sendmsg/<str:username>',views.Sendmsg,name='Sendmsg'),
    path('searchUser/',views.searchUser,name='searchUser'),

]