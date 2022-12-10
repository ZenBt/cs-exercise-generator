from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser
from .forms import CustomUserAdminForm

UserModel = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email']
    list_display_links = ['pk', 'email']
    list_filter = ('email', 'id')
    search_fields = ['email']
    form = CustomUserAdminForm
