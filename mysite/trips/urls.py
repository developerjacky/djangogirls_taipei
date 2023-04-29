from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('post/<pk>', views.post_detail, name='post_detail'),
    path('hello', views.hello, name='hello'),
    path('helloworld', views.helloworld, name='helloworld'),
]
