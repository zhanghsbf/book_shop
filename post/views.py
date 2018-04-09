from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# 写的真丑，有空改改

def index(request):
	"""主页面的视图"""
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
	# 选出浏览量最多的三个商品
	hot_post = Post.objects.all().order_by('-view_times')[0:3]
	categorys = Category.objects.all()

	# 每种商品选择三个浏览量最多的
	cate_post_list = []
	for i in categorys:
		cate_dict = {}		
		cate_post = Post.objects.filter(category=i).order_by('-view_times')[0:3]
		cate_dict['cate'] = i
		cate_dict['post'] = cate_post
		cate_post_list.append(cate_dict)
	return render(request, 'index.html', locals())

def category(request, cate_id):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
	category = Category.objects.get(id=cate_id)
	cate_post = Post.objects.filter(category=category)
	return render(request, 'posts/category.html', locals())

@login_required(login_url='/transfer/')
def write(request):
	"""撰写文章的视图"""
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
		if request.method == 'POST':
			post = Post(user=user)
			post_form = PostForm(request.POST, instance=post)
			if post_form.is_valid():
				post_form.save()
				post.photo1 = request.FILES.get('photo1')
				post.photo2 = request.FILES.get('photo2')
				post.save()
				messages.info(request, '发布成功')
				return redirect('/')
			else:
				messages.info(request, '输入内容有误')
		else:
			post_form = PostForm()
			messages.get_messages(request)
			return render(request, 'posts/write.html', locals())

def posts(request, post_id):
	"""博客文章的详情页面,包括评论功能"""
	post = Post.objects.get(pk=post_id)
	post.view_times += 1
	post.save()
	if request.user.is_authenticated():   #登录了才有评论功能
		username = request.user.username
		user = User.objects.get(username=username)
		if request.method == 'POST':
			comment_form = CommentForm(request.POST)
			if comment_form.is_valid():
				comment = Comment(user=user, post=post, body=request.POST['body'])
				comment.save()
				messages.info(request, '评论已提交')
				return redirect('post:post', post_id=post.id)
			else:
				messages.info(request, '内容有问题')
		else:
			comment_form = CommentForm()

	comments_list = Comment.objects.filter(post=post).order_by('pub_date')
	paginator = Paginator(comments_list, 5)
	page = int(request.GET.get('page',1))
	try:
		comments = paginator.page(page)
	except PageNotAnInteger:
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)

	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	messages.get_messages(request)
	return render(request, 'posts/post.html', locals())

def page_not_found(request):
	return render(request, '404.html')

def user_post(request,user_id):
	post_user = get_object_or_404(User, id=user_id)
	post_list = Post.objects.filter(user=post_user).order_by('-pub_date')
	paginator = Paginator(post_list, 5)
	page = int(request.GET.get('page',1))
	if request.user.is_authenticated():					# 目的是弄出右上角的个人选项，如果不用username的话，未登录的人在模板里的user是anonymous
		username = request.user.username
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	return render(request, 'posts/all_posts.html', locals())

def user_comment(request,user_id):
	comment_user = get_object_or_404(User, id=user_id)
	comment_list = Comment.objects.filter(user=comment_user).order_by('-pub_date')
	paginator = Paginator(comment_list, 5)
	page = int(request.GET.get('page',1))
	if request.user.is_authenticated():
		username = request.user.username
	try:
		comments = paginator.page(page)
	except PageNotAnInteger: 
		comments = paginator.page(1)
	except EmptyPage:
		comments = paginator.page(paginator.num_pages)
	is_first_page = (page == 1)
	is_last_page = (page == paginator.num_pages)
	prev_page = (page - 1)
	next_page = (page + 1)
	total_page = paginator.num_pages

	return render(request, 'posts/all_comments.html', locals())