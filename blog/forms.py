from django import forms
from .models import *
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import List
from blog import models
class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new blog'}))
    description=forms.Textarea()

    class Meta:
        model = Post
        fields=('title','description')
class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields=["item","completed"]

class CreateUserForm(UserCreationForm):
    phone=forms.CharField()
    gender=forms.CharField()
    branch=forms.CharField()
    year=forms.CharField()
    dob=forms.CharField()


    
    class Meta:
        model=User
        fields =['username','email','password1','password2','phone','gender','branch','year','dob']


class profileForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['username','email']
    
class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['status_info']