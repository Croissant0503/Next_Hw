from django.urls import path
from django.views.generic import RedirectView
from bolgApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('category/<str:category>/', views.detail_category, name='category_view'),
    path('', RedirectView.as_view(url='/list/')),  # 루트 URL을 '/list/'로 리다이렉션
]