from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    # path('side-header', views.site_header_component),
    path('about-us', views.AboutView.as_view(), name='about_page')
]
