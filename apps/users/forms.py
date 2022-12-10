from django import forms

from .models import CustomUser


class CustomUserAdminForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'is_active', 'is_superuser', 'is_staff',)
