from django.urls import path
from browser import views

urlpatterns = [
    path('', views.homePage, name="trang-chu"),
    path('thuoc-gia-truyen/', views.thuoc, name="thuoc"),
    path('lien-he/', views.contact, name="lien-he"),
    path('tu-van-suc-khoe/', views.post, name="tu-van-suc-khoe"),
    path('tu-van-suc-khoe/test', views.postDetail, name="tu-van-suc-khoe-detail"),
]
