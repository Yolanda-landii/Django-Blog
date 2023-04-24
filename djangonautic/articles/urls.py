from django.urls import path, re_path
from .import views
# from django.urls import re_path as url


urlpatterns = [
    path('',views.article_list, name="list"),
    re_path('(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
]
