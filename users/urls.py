from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('list/', views.users_list, name='users_list'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]