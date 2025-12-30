from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='نام')
    last_name = forms.CharField(max_length=30, required=True, label='نام خانوادگی')
    email = forms.EmailField(required=False, label='ایمیل')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'نام کاربری',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'خالی بگذارید اگر نمی‌خواهید تغییر کند'}),
        required=False,
        help_text='برای تغییر رمز عبور، مقدار جدید را وارد کنید.'
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active')
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'is_staff': 'دسترسی مدیریتی',
            'is_superuser': 'مدیر کل',
            'is_active': 'فعال',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # رمز عبور قدیمی رو از فرم حذف می‌کنیم (نیازی نیست)
        if 'password' in self.fields:
            del self.fields['password']
        
        for field_name in self.fields:
            field = self.fields[field_name]
            if isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError('رمز عبور و تکرار آن مطابقت ندارند.')
            if not password1:
                raise forms.ValidationError('هر دو فیلد رمز عبور باید پر شوند.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user