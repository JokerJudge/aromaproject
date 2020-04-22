from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from .models import *

# Create your views here.

CONST = {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS}

'''
products = [
		{'name': 'Quartz Belt Watch',
		'image': 'aroma/img/product/product1.png',
		'category': 'Accessories',
		'price': '$150.00'},
		{'name': 'Women Freshwash',
		'image': 'aroma/img/product/product2.png',
		'category': 'Beauty',
		'price': '$10.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product3.png',
		'category': 'Decor',
		'price': '$80.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product4.png',
		'category': 'Decor',
		'price': '$100.00'},
		{'name': 'Man Office Bag',
		'image': 'aroma/img/product/product5.png',
		'category': 'Accessories',
		'price': '$200.00'},
		{'name': 'Charging Car',
		'image': 'aroma/img/product/product6.png',
		'category': 'Kids Toy',
		'price': '$50.00'},
		{'name': 'Blutooth Speaker',
		'image': 'aroma/img/product/product7.png',
		'category': 'Accessories',
		'price': '$99.00'},
		{'name': 'Charger',
		'image': 'aroma/img/product/product8.png',
		'category': 'Accessories',
		'price': '$150.00'}
		]
'''
prod = []
for object in Product.objects.all():
	d = dict(image = object.image,
	name = object.name,
	category = object.category,
	price = object.price)
	prod.append(d)

class IndexView(View):
	def get(self, request):
		carousel_goods = [
		{'name': 'Sneakers',
		'image': 'aroma/img/home/hero-slide1.png'},
		{'name': 'Stylish Headphones',
		'image': 'aroma/img/home/hero-slide2.png'},
		{'name': 'Wireless Speaker',
		'image': 'aroma/img/home/hero-slide3.png'}
		]

		best_sellers = [
		{'name': 'Quartz Belt Watch',
		'image': 'aroma/img/product/product1.png',
		'category': 'Accessories',
		'price': '$150.00'},
		{'name': 'Women Freshwash',
		'image': 'aroma/img/product/product2.png',
		'category': 'Beauty',
		'price': '$10.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product3.png',
		'category': 'Decor',
		'price': '$80.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product4.png',
		'category': 'Decor',
		'price': '$100.00'},
		{'name': 'Quartz Belt Watch',
		'image': 'aroma/img/product/product1.png',
		'category': 'Accessories',
		'price': '$150.00'},
		{'name': 'Women Freshwash',
		'image': 'aroma/img/product/product2.png',
		'category': 'Beauty',
		'price': '$10.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product3.png',
		'category': 'Decor',
		'price': '$80.00'},
		{'name': 'Room Flash Light',
		'image': 'aroma/img/product/product4.png',
		'category': 'Decor',
		'price': '$100.00'}
		]
		
		news = [
		{'title': 'The Richland Center Shooping News and weekly shooper',
		'image': 'aroma/img/blog/blog1.png',
		'author': 'By Putin',
		'comments_counter': '36 Comments',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'},
		{'title': 'The Shopping News also offers top-quality printing services',
		'image': 'aroma/img/blog/blog2.png',
		'author': 'By Navalnyi',
		'comments_counter': '2 Comments',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'},
		{'title': 'Professional design staff and efficient equipment you’ll find we offer',
		'image': 'aroma/img/blog/blog3.png',
		'author': 'By Soloviev',
		'comments_counter': '5 Comments',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'}
		]
		
		return render(request, 'aroma/index.html', {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS,
		'carousel_goods': carousel_goods,
		'prod': prod,
		'best_sellers': best_sellers,
		'news': news})

class BlogView(View):
	def get(self, request):
		
		categories = [
		{'title': 'Social Life',
		'image': 'aroma/img/blog/cat-post/cat-post-3.jpg',
		'description': 'Enjoy your social life together'},
		{'title': 'Politics',
		'image': 'aroma/img/blog/cat-post/cat-post-2.jpg',
		'description': 'Be a part of politics'},
		{'title': 'Food',
		'image': 'aroma/img/blog/cat-post/cat-post-1.jpg',
		'description': 'Let the food be finished'}
		]
		
		articles = [
		{'author': 'Mark wiens',
		'date': '12 Dec, 2017',
		'views': '1.2M Views',
		'comments': '06 Comments',
		'title': 'Astronomy Binoculars A Great Alternative',
		'image': 'aroma/img/blog/main-blog/m-blog-1.jpg',
		'description': '''MCSE boot camps have its supporters and its detractors. Some people do not understand
                                          why you should have to spend money on boot camp when you can get the MCSE study
                                          materials yourself at a fraction.'''},
		{'author': 'Mark wiens',
		'date': '15 Dec, 2019',
		'views': '1.5M Views',
		'comments': '43 Comments',
		'title': 'The Basics Of Buying A Telescope',
		'image': 'aroma/img/blog/main-blog/m-blog-2.jpg',
		'description': '''MCSE boot camps have its supporters and its detractors. Some people do not understand
                                          why you should have to spend money on boot camp when you can get the MCSE study
                                          materials yourself at a fraction.'''},
		{'author': 'Mark wiens',
		'date': '13 Nov, 2018',
		'views': '0.6M Views',
		'comments': '15 Comments',
		'title': 'The Glossary Of Telescopes',
		'image': 'aroma/img/blog/main-blog/m-blog-3.jpg',
		'description': '''MCSE boot camps have its supporters and its detractors. Some people do not understand
                                          why you should have to spend money on boot camp when you can get the MCSE study
                                          materials yourself at a fraction.'''},
		{'author': 'Mark wiens',
		'date': '12 Dec, 2017',
		'views': '1.2M Views',
		'comments': '06 Comments',
		'title': 'The Night Sky',
		'image': 'aroma/img/blog/main-blog/m-blog-4.jpg',
		'description': '''MCSE boot camps have its supporters and its detractors. Some people do not understand
                                          why you should have to spend money on boot camp when you can get the MCSE study
                                          materials yourself at a fraction.'''},
		{'author': 'Mark wiens',
		'date': '12 Dec, 2017',
		'views': '1.2M Views',
		'comments': '06 Comments',
		'title': 'Telescopes 101',
		'image': 'aroma/img/blog/main-blog/m-blog-5.jpg',
		'description': '''MCSE boot camps have its supporters and its detractors. Some people do not understand
                                          why you should have to spend money on boot camp when you can get the MCSE study
                                          materials yourself at a fraction.'''}
		]
		
	
		return render(request, 'aroma/blog.html', {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS,
		'categories': categories,
		'articles': articles
		})

class CartView(View):
	def get(self, request):
		
		cart = [
		{'name': 'Bluetooth speaker',
		'image': 'aroma/img/cart/cart1.png',
		'price': '$99.00',
		'description': 'Irritation for your neighbours',
		'quantity': '1',
		'total': '$99.00'},
		{'name': 'Sneakers',
		'image': 'aroma/img/cart/cart2.png',
		'price': '$150.00',
		'description': 'Hey, lazy! Try to go to gym!',
		'quantity': '1',
		'total': '$150.00'},
		{'name': 'Charging Car',
		'image': 'aroma/img/cart/cart3.png',
		'price': '$50.00',
		'description': 'Good stuff for your baby',
		'quantity': '1',
		'total': '$50.00'},
		]
		
		
		return render(request, 'aroma/cart.html', {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS,
		'cart': cart
		})

class CategoryView(View):
	def get(self, request):
		
		
		top_products = [
		{'name': 'Glass',
		'image': 'aroma/img/product/product-sm-1.png',
		'price': '$5.00'},
		{'name': 'Bulb',
		'image': 'aroma/img/product/product-sm-2.png',
		'price': '$8.00'},
		{'name': 'Small carpet',
		'image': 'aroma/img/product/product-sm-3.png',
		'price': '$5.00'},
		{'name': 'Toothbrush',
		'image': 'aroma/img/product/product-sm-4.png',
		'price': '$6.00'},
		{'name': 'Cream',
		'image': 'aroma/img/product/product-sm-5.png',
		'price': '$5.00'},
		{'name': 'Handler',
		'image': 'aroma/img/product/product-sm-6.png',
		'price': '$12.00'},
		{'name': 'Pregnancy test',
		'image': 'aroma/img/product/product-sm-7.png',
		'price': '$4.00'},
		{'name': 'Chair',
		'image': 'aroma/img/product/product-sm-8.png',
		'price': '$25.00'},
		{'name': 'Interior stuff',
		'image': 'aroma/img/product/product-sm-9.png',
		'price': '$15.00'},
		{'name': 'Glass',
		'image': 'aroma/img/product/product-sm-1.png',
		'price': '$5.00'},
		{'name': 'Bulb',
		'image': 'aroma/img/product/product-sm-2.png',
		'price': '$8.00'},
		{'name': 'Small carpet',
		'image': 'aroma/img/product/product-sm-3.png',
		'price': '$5.00'}
		]
			
		return render(request, 'aroma/category.html', {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS,
		'prod': prod
		})

class CheckoutView(View):
	def get(self, request):
		return render(request, 'aroma/checkout.html', CONST)

class ConfirmationView(View):
	def get(self, request):
		return render(request, 'aroma/confirmation.html', CONST)

class ContactView(View):
	def get(self, request):
		return render(request, 'aroma/contact.html', CONST)

class LoginView(View):
	def get(self, request):
		return render(request, 'aroma/login.html', CONST)

class RegisterView(View):
	def get(self, request):
		return render(request, 'aroma/register.html', CONST)

class SingleBlogView(View):
	def get(self, request):
		return render(request, 'aroma/single-blog.html', CONST)

class SingleProductView(View):
	def get(self, request):
		
		reviews = [
		{'image': 'aroma/img/product/review-1.png',
		'author': 'By Putin',
		'datetime': '12th Feb, 2018 at 05:56 pm',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'},
		{'image': 'aroma/img/product/review-2.png',
		'author': 'By Navalnyi',
		'datetime': '12th Feb, 2018 at 05:56 pm',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'},
		{'image': 'aroma/img/product/review-3.png',
		'author': 'By Soloviev',
		'datetime': '12th Feb, 2018 at 05:56 pm',
		'main_text': 'Let one fifth i bring fly to divided face for bearing divide unto seed. Winged divided light Forth.'}
		]
		
		return render(request, 'aroma/single-product.html', {'site_name': SITE_NAME,
		'phone_number': PHONE_NUMBER,
		'email': EMAIL,
		'site_url': SITE_URL,
		'address': ADDRESS,
		'reviews': reviews
		})

class TrackingOrderView(View):
	def get(self, request):
		return render(request, 'aroma/tracking-order.html', CONST)