from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def register_request_view(request):
    return render(request, 'dashboard/register_request.html')  # صفحه ثبت درخواست (بعداً فرم اضافه کنید)

@login_required
def track_request_view(request):
    return render(request, 'dashboard/track_request.html')  # صفحه پیگیری (بعداً منطق اضافه کنید)

@login_required
def list_requests_view(request):
    return render(request, 'dashboard/list_requests.html')  # صفحه لیست (بعداً داده‌ها اضافه کنید)

@login_required
def ai_assistant_view(request):
    return render(request, 'dashboard/ai_assistant.html')  # صفحه AI (بعداً интеграция اضافه کنید)