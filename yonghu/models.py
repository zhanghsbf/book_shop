import random
from django.db import models
from django.contrib.auth.models import User

# 用户的资料
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.CharField(max_length=10, blank=True)
	age = models.IntegerField(null=True, blank=True)
	is_boy = models.NullBooleanField(null=True, blank=True)
	note = models.TextField(null=True, blank=True)
	head_cut = models.ImageField(default='/media/head_cuts/default.jpg' ,upload_to='head_cuts')
	
	def __str__(self):
		return self.user.username

# 增加测试用户
def add_robot(x,y):
	for i in range(x,y):
		name = 'robot%s' %i
		robot = User(username=name, password='cat', is_active=1)
		robot.save()
		robot_profile = Profile(user=robot,nickname=robot.username)
		robot_profile.save()
		print(robot)

