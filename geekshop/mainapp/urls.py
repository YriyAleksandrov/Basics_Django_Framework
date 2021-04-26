from django.urls import path
from .views import main, products, contacts


urlpatterns = [
    path('', main),
    path('index/', main),
    path('products/', products),
    path('contact/', contacts),
]