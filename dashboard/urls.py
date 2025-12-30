from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # صفحه اصلی dashboard با منو
    path('register-request/', views.register_request_view, name='register_request'),  # placeholder برای ثبت درخواست
    path('track-request/', views.track_request_view, name='track_request'),  # placeholder برای پیگیری
    path('list-requests/', views.list_requests_view, name='list_requests'),  # placeholder برای لیست
    path('ai-assistant/', views.ai_assistant_view, name='ai_assistant'),  # placeholder برای AI
]