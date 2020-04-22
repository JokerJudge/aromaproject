from django.urls import path
from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('blog/', BlogView.as_view(), name='blog'),
	path('cart/', CartView.as_view(), name='cart'),
	path('category/', CategoryView.as_view(), name='category'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
	path('contact/', ContactView.as_view(), name='contact'),
	path('login/', LoginView.as_view(), name='login'),
	path('register/', RegisterView.as_view(), name='register'),
	path('single-blog/', SingleBlogView.as_view(), name='single-blog'),
	path('single-product/', SingleProductView.as_view(), name='single-product'),
	path('tracking-order/', TrackingOrderView.as_view(), name='tracking-order')
]
