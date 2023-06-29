from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('homeAll/',views.homeAll,name='homeAll'),
    path('orgAll/',views.orgAll,name='orgAll'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add/',views.add,name='add'),
    path('delete/<int:postId>', views.delete, name='delete'),
    path('edit/<int:postId>', views.edit, name='edit'),
    path('like/<int:postId>', views.like, name='like'),
    path('details/<int:postId>', views.details, name='details'),
    path('cmnt/<int:postId>', views.cmnt, name='cmnt'),

    path('comment/<int:postId>', views.comment, name='comment'),
    path('profile/<str:username>',views.userProfile, name='userProfile'),
    path('postfollowers/<str:username>',views.postfollowers, name='postfollowers'),

    path('profileAnony/<str:username>',views.userProfileAnony, name='userProfileAnony'),
    path('follow/<str:username>',views.follow, name='follow'),
    path('follower/<str:username>',views.follower, name='follower'),
    path('following/<str:username>',views.following, name='following'),
    path('changepass/',views.change_pass,name="changepass"),


  
]