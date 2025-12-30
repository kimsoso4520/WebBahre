from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # دسترسی فقط برای کاربران لاگین‌شده
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')  # صفحه اصلی با منو

@login_required
def register_request_view(request):
    # پروسه خاص: مثلاً فرم ثبت درخواست با مدل Request
    return render(request, 'dashboard/register_request.html')

@login_required
def track_request_view(request):
    # پروسه خاص: جستجو و نمایش وضعیت درخواست
    return render(request, 'dashboard/track_request.html')

@login_required
def list_requests_view(request):
    # پروسه خاص: لیست درخواست‌ها با فیلتر و pagination
    return render(request, 'dashboard/list_requests.html')

@login_required
def ai_assistant_view(request):
    # پروسه خاص: интеграция با AI (مثل API یا مدل محلی)
    return render(request, 'dashboard/ai_assistant.html')