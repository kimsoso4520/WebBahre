from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CustomUserChangeForm  # این خط رو اضافه کن
from django import forms
from django.contrib.messages.views import SuccessMessageMixin


# لیست کاربران
def users_list(request):
    User = get_user_model()
    users = User.objects.all().order_by('-date_joined')
    
    context = {
        'users': users,
    }
    return render(request, 'admin/users_list.html', context)

# افزودن کاربر جدید
class UserCreateView(CreateView):
    model = get_user_model()  # اینجا از get_user_model استفاده می‌کنیم
    form_class = CustomUserCreationForm
    template_name = 'admin/user_create.html'
    success_url = reverse_lazy('users:users_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # اضافه کردن فیلدهای نقش و وضعیت
        form.fields['is_staff'] = forms.BooleanField(required=False, label='دسترسی مدیریتی (staff)')
        form.fields['is_superuser'] = forms.BooleanField(required=False, label='مدیر کل (superuser)')
        form.fields['is_active'] = forms.BooleanField(required=False, initial=True, label='کاربر فعال باشد')
        
        # استایل چک‌باکس‌ها
        form.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        form.fields['is_superuser'].widget.attrs.update({'class': 'form-check-input'})
        form.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})
        
        return form

    def form_valid(self, form):
        messages.success(self.request, 'کاربر با موفقیت اضافه شد.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'لطفاً خطاها را برطرف کنید.')
        return super().form_invalid(form)


# ویرایش کاربر
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'admin/user_edit.html'
    success_url = reverse_lazy('users:users_list')
    success_message = 'اطلاعات کاربر با موفقیت بروزرسانی شد.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object  # برای نمایش نام در عنوان صفحه
        return context

# حذف کاربر
class UserDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('users:users_list')

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, 'کاربر با موفقیت حذف شد.')
        return super().form_valid(request, *args, **kwargs)