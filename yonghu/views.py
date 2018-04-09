from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def login(request):
	if request.method == "POST":
		user = authenticate(username=request.POST['username'],\
							password=request.POST['password'])
		if user is not None:
			if user.is_active:
				username = user.username
				auth.login(request, user)
				messages.info(request, '登录成功！')
				# 登录时判断用户是否有资料模型，没有则创建一个
				has_p = models.Profile.objects.filter(user=user).first()
				if has_p is None:
					cre_p = models.Profile(user=user,nickname=user.username)
					cre_p.save()
				return redirect('/')
			else:
				messages.info(request, '账号未激活，请去邮箱激活...')
		else:
			messages.warning(request, '账号不存在，或用户名/密码错误...')

	return render(request, 'yonghu/login.html')

@login_required(login_url='/transfer/')
def logout(request):
	auth.logout(request)
	messages.info(request, "成功注销...")
	return redirect('/')


# @login_required(login_url="/transfer/")
def profile(request, user_id):
	'''
		展示用户资料，关注取关用户，以及修改用户资料
	'''
	profile_user = get_object_or_404(User, pk=user_id)			# 拿到当前页面的用户对象

	try:
		profile = models.Profile.objects.get(user=profile_user)
	except:
		profile = models.Profile(user=profile_user)
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)	# 拿到数据库中的当前用户对象
		is_mine_profile = user == profile_user
		if request.method == 'POST':
			# 只有当前用户等于登录用户时模板才显示修改表单
			old_nickname = user.profile.nickname
			if request.POST['nickname'] == '':
				request.POST['nickname'] = user.profile.nickname
			profile_form = forms.ProfileForm(request.POST, instance=profile)
			if profile_form.is_valid():
				profile_form.save()
				profile.head_cut = request.FILES.get('head_cut')						# 不知为何用ModelForm保存文件没用
				if profile.head_cut != None:
					profile.save()
			messages.info(request, '个人资料已储存')
			return redirect('yonghu:profile', user_id=user.id)
			# else:
			# 	messages.info(request, '资料全都要填')
		else:
			profile_form = forms.ProfileForm()
	messages.get_messages(request)

	return render(request, 'yonghu/profile.html', locals())


# login_required提示页面
def login_required_transfer(request):
	return render(request, 'yonghu/login_required_transfer.html')
