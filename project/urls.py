from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('new/', views.new, name='new'),
   path('detail/<int:post_pk>', views.detail, name='detail'),
   path('edit/<int:post_pk>', views.edit, name='edit'),
   path('delete/<int:post_pk>', views.delete, name='delete'),
   path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
   path("registration/signup/", views.signup, name="signup"),
   path("registration/login/", views.login, name="login"),
   path("registration/logout/", views.logout, name="logout"),
   path("like", views.like, name="like"),
   path('add_comment', views.add_comment, name='add_comment'),
   path('delete_comment/<int:comment_pk>', views.delete_comment, name='delete_comment'),
   path('edit_comment/<int:comment_pk>', views.edit_comment, name='edit_comment'),
]
