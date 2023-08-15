from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('about', views.about),
    path('contact', views.contact),
    path('category/<int:pk>', views.get_exact_category),
    path('product/<int:pk>', views.get_exact_product),
    path('search', views.search_product),
]