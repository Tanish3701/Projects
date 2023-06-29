from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Comment,Follower,Following,List,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from . forms import PostForm,ListForm,CreateUserForm,profileForm,UpdateProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def homeAll(request):
    posts=Post.objects.all()
    data={'posts':posts}
    return render(request,'blog/allpost.html',data)
def orgAll(request):
    posts=Post.objects.all()
    data={'posts':posts}
    return render(request,'blog/organization.html',data)
def change_pass(request):
    if request.method =="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'password changed successfully')
            return redirect('/blog')
    else:

        fm=PasswordChangeForm(user=request.user)
    return render(request,'blog/changepass.html',{'form':fm})
@login_required

def edit_profile(request):
    if request.method =="POST":
        form=profileForm(data=request.POST,instance=request.user)
        update=form.save()
       
        update.save()
        return redirect('/blog')
    else:
        form=profileForm(instance=request.user)
    return render(request,'blog/edit_profile.html',{'form':form})
        
def home(request):
    user=request.user

    follow1,create = Following.objects.get_or_create(user=user)
    following_name=follow1.following.all()

    posts=Post.objects.filter(author__in=following_name).order_by('-pk')
    data={'posts':posts}
    return render(request,'blog/home.html',data)

def userProfileAnony(request,username):
    user = User.objects.filter(username=username)
    posts = Post.objects.filter(author=user[0])
    follow1,create = Following.objects.get_or_create(user=user[0])
    follow2,create = Follower.objects.get_or_create(user=user[0])
    following_count=follow1.following.count()
    follower_count=follow2.followers.count()
    data={'posts':posts,
          'username':username,
          'following_count':following_count,
          'follower_count':follower_count
          }
    return render(request,'blog/userProfileAnony.html',data)


def userProfile(request,username):
        
        if request.method == 'POST':
            p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if p_form.is_valid():
                p_form.save()
                messages.success(request,f'Your Profile has been updated!')
                
                return redirect('/')
        else:
            p_form= UpdateProfileForm(instance=request.user.profile)
            person = User.objects.get(username = username)


        user=User.objects.filter(username=username)
        mainUser=request.user
        
        
        posts=Post.objects.filter(author=user[0])
        flwng=Following.objects.filter(user=mainUser,following=user[0])
        is_following= True if flwng else False
        flag=True if str(request.user) == str(username) else False

        #fetching follower's count, following's count, follower's list, following's list
        follow1,create = Following.objects.get_or_create(user=user[0])
        follow2,create = Follower.objects.get_or_create(user=user[0])
        #follow1 = Following.objects.get(user=user[0])
        #follow2 = Follower.objects.get(user=user[0])
        following_name=follow1.following.all()
        follower_name=follow2.followers.all()
        following_count=follow1.following.count()
        follower_count=follow2.followers.count()


        data={'posts':posts,
            'username':username,
            'is_following':is_following,
            'flag':flag,
            'person':person,
            'p_form':p_form,
            'following_count':following_count,
            'follower_count':follower_count
            }
        print('username:',username,'user: ', mainUser,'flag: ',flag)
        #for post in posts:
            #print(post.like.count())
        return render(request,'blog/profile.html',data)
def postfollowers(request,username):

    
    user=User.objects.filter(username=username)
    follow1 = Following.objects.get(user=user[0])
  
    
    follows_users =follow1.following.all()
    posts = Post.objects.filter(author_id__in=follows_users)


    data={'posts':posts,
          'username':username,
          }
    return render(request,'blog/postfollowers.html',data)
    
def add(request):

    if request.method=='POST':
        user_=request.user
        title_=request.POST.get('title')
        description_=request.POST.get('description')

        post_obj= Post(author=user_,title=title_,description=description_)
        post_obj.save()
        return redirect('/blog')

def delete(request, postId):
    post_ = Post.objects.filter(pk=postId)  # pk=primary key

    post_.delete()

    return redirect('/blog')


    
def edit(request, postId):
    post = Post.objects.get(id=postId)

    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/blog')

    context = {'form': form}

    return render(request, 'blog/update_post.html', context)

def like(request, postId):


    post = Post.objects.get(pk=postId)
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)


    #post.save()
    return redirect('/blog')

def details(request,postId):
    post=Post.objects.get(pk=postId)
    comments=Comment.objects.filter(post=post)
    context={'post':post,'comments':comments}
    return render(request,'blog/details.html',context)

def cmnt(request,postId):
    post=Post.objects.get(pk=postId)
    comments=Comment.objects.filter(post=post)
    context={'post':post,'comments':comments}
    return render(request,'blog/comment.html',context)

def comment(request,postId):
    post=Post.objects.get(pk=postId)
    if request.method=='POST':
        user_=request.user
        body_=request.POST.get('comment')
        cmnt_obj=Comment(viewer=user_,post=post,body=body_)
        cmnt_obj.save()
    return redirect('/blog')

def follow(request,username):
    user2 = User.objects.get(username=username)
    user1 = request.user
    # user1 wants to follow user2

    flwng=Following.objects.filter(user=user1,following=user2)
    is_following= True if flwng else False
    print(is_following)


    #adding user2 to following list of user1
    follow1,create = Following.objects.get_or_create(user=user1)
    follow2,create = Follower.objects.get_or_create(user=user2)
    if is_following:
        follow2.followers.remove(user1)
        follow1.following.remove(user2)
    else:
        follow2.followers.add(user1)
        follow1.following.add(user2)
    return HttpResponse('Followed')


def follower(request,username):
    user = User.objects.filter(username=username)
    follow2 = Follower.objects.get(user=user[0])
    follower_name=follow2.followers.all()
    context={
        'work':'Followers',
        'names':follower_name,
    }
    return render(request,'blog/followed.html',context)


def following(request, username):
    user = User.objects.filter(username=username)
    follow1 = Following.objects.get(user=user[0])
    following_name = follow1.following.all()
    context = {
        'work': 'Following',
        'names': following_name,

    }
    return render(request, 'blog/followed.html', context)

#<!--<a href="{% url 'follow' post.author %}">Follow</a>-->