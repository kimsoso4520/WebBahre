from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # بخش ویرایش کاربر
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'is_staff_member', 'role')}),
    )

    # بخش اضافه کردن کاربر
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'phone_number', 'is_staff_member', 'role',
                'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

    # ستون‌های لیست کاربران
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'is_staff_member', 'is_active')
    list_filter = ('role', 'is_staff_member', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role', 'phone_number')

    # محدود کردن دسترسی کاربران به لیست
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'manager':
            return qs  # Manager همه کاربران را می‌بیند
        elif request.user.role == 'staff':
            return qs.filter(role='employee')  # Staff فقط کاربران Employee را می‌بینند
        else:
            return qs.none()  # سایر Roleها دسترسی ندارند

    # دسترسی به اضافه کردن کاربر
    def has_add_permission(self, request):
        return request.user.role in ['manager', 'staff']

    # دسترسی به ویرایش کاربر
    def has_change_permission(self, request, obj=None):
        if request.user.role == 'manager':
            return True
        elif request.user.role == 'staff' and obj and obj.role == 'employee':
            return True
        return False

    # دسترسی به حذف کاربر
    def has_delete_permission(self, request, obj=None):
        return request.user.role == 'manager'

# ثبت CustomUser در Admin
admin.site.register(CustomUser, CustomUserAdmin)
