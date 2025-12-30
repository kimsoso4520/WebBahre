from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # صفحه اصلی داشبورد
    path('register-request/', views.register_request_view, name='register_request'),  # ثبت درخواست
    path('track-request/', views.track_request_view, name='track_request'),  # پیگیری درخواست
    path('list-requests/', views.list_requests_view, name='list_requests'),  # لیست درخواست‌ها
    path('ai-assistant/', views.ai_assistant_view, name='ai_assistant'),  # دستیار هوش مصنوعی
]