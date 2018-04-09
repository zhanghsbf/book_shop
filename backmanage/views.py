from django.shortcuts import render
from django.http import HttpResponse
import json
from post.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


@csrf_exempt
def manage(request):
	return render(request, 'backmanage/manage.html')

@csrf_exempt
def book_data(request):
	sort = request.POST.get('sort',None)
	order = request.POST.get('order','asc')
	category_id = request.POST.get('category_id', None)

	posts = Post.objects.all()
	if category_id is not None:
		posts = posts.filter(category_id = category_id)
		print(posts)
	posts_list = Paginator(posts, request.POST.get('row',10))
	page = request.POST.get('page', 1)
	response = {}
	response['total'] = posts_list.count
	data = []
	for i in posts_list.page(page):
		dirs = {}
		dirs['category'] = i.category.name
		dirs['user'] = i.user.profile.nickname
		dirs['title'] = i.title
		dirs['price'] = i.price
		dirs['pub_date'] = i.pub_date.strftime("%Y/%m/%d %H:%M:%S")
		dirs['view_times'] = i.view_times
		data.append(dirs)
	response['rows'] = data
	return HttpResponse(json.dumps(response))

@csrf_exempt
def manage_category(request):
	categorys = Category.objects.all()
	category_list = []
	for i in categorys:
		dirs = {}
		dirs['id'] = i.id
		dirs['text'] = i.name
		category_list.append(dirs)
	return HttpResponse(json.dumps(category_list))

@csrf_exempt
def manage_user(request):
	users = User.objects.all()
	user_list = []
	for i in users:
		dirs = {}
		dirs['id'] = i.id
		dirs['text'] = i.profile.nickname
		user_list.append(dirs)
	return HttpResponse(json.dumps(user_list))

@csrf_exempt
def manage_user_sub(request):
	user = User.objects.get(id=request.POST['user'])
	category = Category.objects.get(id=request.POST['category'])
	title = request.POST['title']
	body = request.POST['body']
	price = request.POST['price']
	origin_price = request.POST['origin_price']
	post = Post(user=user,category=category,title=title,body=body,price=price,origin_price=origin_price)
	post.save()
	return HttpResponse('添加成功')

@csrf_exempt
def manage_user_del(request):
	user = User.objects.get(id=request.POST['user'])
	category = Category.objects.get(id=request.POST['category'])
	title = request.POST['title']
	body = request.POST['body']
	price = request.POST['price']
	origin_price = request.POST['origin_price']
	post = Post(user=user,category=category,title=title,body=body,price=price,origin_price=origin_price)
	post.save()
	return HttpResponse('添加成功')