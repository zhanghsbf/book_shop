from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from post.models import *


@login_required(login_url='/transfer/')
def add_to_buycar(request, post_id):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
	# 拿到商品数据
	post = get_object_or_404(Post, id=post_id)
	buycar = request.session.get('buycar',None)
	if buycar == None:
		buycar = request.session['buycar'] = []
		print(buycar,123)
	buycar.append(post.id)
	request.session['buycar'] = buycar
	messages.info(request, '成功添加商品：{}'.format(post.title))
	return redirect('/')

@login_required(login_url='/transfer/')
def show_buycar(request):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
	# 取出购物车内的商品id
	buycar = request.session['buycar']
	print('show',buycar)
	post_list = []
	total = 0
	for i in buycar:
		post = Post.objects.get(id=i)
		post_list.append(post)
		total += post.price

	return render(request, 'buy/buycar.html', locals())


@login_required(login_url='/transfer/')
def add_order(request):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
		if request.method == 'POST':
			total = request.POST['total']
			address = request.POST['address']
			order = Order(buyer=user,total=total,address=address)
			order.save()
			# 订单的每个商品
			buycar = request.session['buycar']
			for i in buycar:
				post = Post.objects.get(id=i)
				item = OrderItem(order=order, seller=post.user, post=post, price=post.price)
				item.save()
			messages.info(request, '订单创建成功！')
			return redirect('index')



@login_required(login_url='/transfer/')
def user_order(request):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
		# 获取用户提交的的订单
		orders = Order.objects.filter(buyer=user)
		order_list = []
		for i in orders:
			x = {}
			x['order'] = i
			x['items'] = i.orderitem_set.all()
			order_list.append(x)

		# 获取用户被下单的商品
		items = OrderItem.objects.filter(seller=user)
		print(items)
		return render(request, 'buy/user_order.html', locals())

def order(request, order_id):
	if request.user.is_authenticated():
		username = request.user.username
		user = User.objects.get(username=username)
	order = Order.objects.get(id=order_id)
	items = OrderItem.objects.filter(order=order)
	return render(request, 'buy/order.html', locals())

def item_confirm(request, item_id):
	item = OrderItem.objects.get(id=item_id)
	item.confirm_item()
	return redirect('buy:user_order')

def item_send(request, item_id):
	item = OrderItem.objects.get(id=item_id)
	item.send_out_goods()
	return redirect('buy:user_order')

def item_receive(request, item_id):
	item = OrderItem.objects.get(id=item_id)
	item.receive_goods()
	return redirect('buy:user_order')