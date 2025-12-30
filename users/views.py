from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# لیست کاربران - فقط برای مدیران
@method_decorator(staff_member_required, name='dispatch')
class UsersListView(ListView):
    model = get_user_model()
    template_name = 'admin/users_list.html'
    context_object_name = 'users'
    ordering = ['-date_joined']
    paginate_by = 20  # هر صفحه ۲۰ کاربر

    def get_queryset(self):
        return get_user_model().objects.all().order_by('-date_joined')


# افزودن کاربر جدید - فقط برای مدیران
@method_decorator([login_required, staff_member_required], name='dispatch')
class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'admin/user_create.html'
    success_url = reverse_lazy('users:users_list')
    success_message = 'کاربر با موفقیت اضافه شد.'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # اضافه کردن چک‌باکس‌های نقش و وضعیت
        form.fields['is_staff'] = forms.BooleanField(required=False, label='دسترسی مدیریتی (staff)')
        form.fields['is_superuser'] = forms.BooleanField(required=False, label='مدیر کل (superuser)')
        form.fields['is_active'] = forms.BooleanField(required=False, initial=True, label='کاربر فعال باشد')

        # استایل چک‌باکس‌ها
        form.fields['is_staff'].widget.attrs.update({'class': 'form-check-input'})
        form.fields['is_superuser'].widget.attrs.update({'class': 'form-check-input'})
        form.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})

        return form


# ویرایش کاربر - فقط برای مدیران
@method_decorator([login_required, staff_member_required], name='dispatch')
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


# حذف کاربر - فقط برای مدیران
@method_decorator([login_required, staff_member_required], name='dispatch')
class UserDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('users:users_list')

    def form_valid(self, form):
        messages.success(self.request, 'کاربر با موفقیت حذف شد.')
        return super().form_valid(form)



class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    redirect_authenticated_user = True



def custom_logout(request):
    logout(request)
    return redirect('users:login')