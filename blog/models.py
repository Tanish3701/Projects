from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)

	status_info = models.CharField(default="Enter status", max_length=1000)
	



	def __str__(self):
		return f'{self.user.username} Profile'

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title+' | '+str(self.author)

class List(models.Model):
    item=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

def __str__(self):
    return self.item + ' | ' + str(self.completed)

class Comment(models.Model):
    viewer = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    def __str__(self):
        return self.post.title+' | '+str(self.viewer)

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers')

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followings')



