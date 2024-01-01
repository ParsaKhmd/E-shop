from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='products_categories_list'),
    path('brands/<brand>', views.ProductListView.as_view(), name='products_list_by_brands'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),

]
