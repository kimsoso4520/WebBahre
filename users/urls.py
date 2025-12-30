from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('list/', views.UsersListView.as_view(), name='users_list'),  # تغییر به Class-Based
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]