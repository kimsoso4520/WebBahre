from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_dashboard(request):
    return redirect('dashboard')  # نام URL داشبورد اصلی

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', redirect_to_dashboard),  # ریشه سایت به داشبورد ریدایرکت می‌شه
]