from django.urls import path
from django.views.generic import RedirectView
from bolgApp import views
from django.contrib import admin
from bolgApp.views import signup
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('category/<str:category>/', views.detail_category, name='category_view'),
    path('', RedirectView.as_view(url='/list/')),  # 루트 URL을 '/list/'로 리다이렉션
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('allauth.urls')),

]