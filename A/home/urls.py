from django.urls import path
from . import views

app_name ='home'
urlpatterns = [
    
    path('',views.Home.as_view(),name='home'),
    path('<slug:slug>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('category/<slug:category_slug>/,',views.Home.as_view(),name='category_filter')

]