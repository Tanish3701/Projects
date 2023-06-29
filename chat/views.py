
from django.shortcuts import render,HttpResponse,redirect
from .models import Message
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def chatHome(request,username):
    to_user= User.objects.filter(username=username)
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=to_user[0])


    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        'username':username,
    }
    return render(request,'chat/chat.html',context)

def recipient(request):
    message=Message.get_messages(user=request.user)
    context={'message':message}
    return render(request,'chat/recipient.html',context)

def searchUser(request):

    query = request.GET.get("q")
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination, 100- 100 users per page
        paginator = Paginator(users, 3 )
        page = request.GET.get('page')
        users_paginator = paginator.get_page(page)

        context = {
            'quser':query,
            'users': users_paginator,
        }

    return render(request, 'chat/search_user.html',context)

def Sendmsg(request,username):
    from_user=request.user
    to_user = User.objects.filter(username=username)
    body=request.POST.get('msg')
    sender_msg=Message.send_message(from_user=from_user,to_user=to_user[0],body=body)
    return redirect('chathome',username)


