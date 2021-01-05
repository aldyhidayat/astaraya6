from django.urls import path
from .views import *

app_name='store'
urlpatterns=[
	path('keranjang', cart, name='cart'),
	path('bayar', checkout, name='checkout'),
	path('update_item/', updateItem, name='update_item'),

	path('process_order/', processOrder, name='processOrder'),	
	path('', PerempuanListView.as_view(), name='home'),
	path('detail/<int:slug>', ProductDetailView.as_view(), name='detail'),
	path('store/<page>', PerempuanListView.as_view(), name='perempuan'),
]
