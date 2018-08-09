# from django.conf.urls import url
# from . import views


# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
#     url('post/<int:pk>/', views.post_detail, name='post_detail'),
# ]


from django.urls import path, include
from django.contrib import admin
from blog import views


urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]