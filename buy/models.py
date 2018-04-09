from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Order(models.Model):
	buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.DO_NOTHING)
	total = models.FloatField()
	address = models.CharField(max_length=50)
	generate_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{0},date{1}".format(self.buyer, self.generate_date)

class OrderItem(models.Model):
	seller = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	price = models.FloatField()
	status = models.IntegerField(default=0)

	# item状态 0:已提交, 1:已确认， 2：已发货, 3:已收货
	def confirm_item(self):
		self.status += 1
		self.save()
	def send_out_goods(self):
		self.status += 1
		self.save()
	def receive_goods(self):
		self.status += 1
		self.save()

	def __str__(self):
		return self.post.title