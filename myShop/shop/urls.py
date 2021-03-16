from django.urls import path
from .import views


urlpatterns = [
    path('', views.index,name='shopHome'),
    path('about/', views.about,name='AboutUs'),
    path('contact/', views.contact,name='ContactUs'),
    path('search/', views.search,name='Search'),
    path('products/<int:myid>', views.productView,name='ProductView'),
    path('checkout/', views.checkout,name='Checkout'),
    path('successful/', views.successful,name='successful'),


]