# Django-Blog-master/admin/urls.py
from django.urls import path
from .views import CustomAdminLoginView,admin_dashboard,CustomLogoutView,UsersListView, BlogListView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from .views import block_user,remove_user,blog_list
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('custom-admin/login/', CustomAdminLoginView.as_view(), name='admin-login'),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('custom-admin/login/', CustomAdminLoginView.as_view(), name='admin-login'),
    path('custom-admin/login/', CustomAdminLoginView.as_view(), name='admin-login'),
    path('admin/users/', UsersListView.as_view(), name='users-list'),  # Add this line
    path('admin/blogs/', BlogListView.as_view(), name='blog-list'),
    path('block_user/<int:user_id>/', block_user, name='block_user'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('remove_user/<int:user_id>/', remove_user, name='remove_user'),
    path('blogs/', blog_list, name='blog_list'),
    
    
]


