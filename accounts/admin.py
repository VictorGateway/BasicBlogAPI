from django.contrib import admin
from .models import CustomUser
from .forms import CustomChangeForm, CustomCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomAdmin(UserAdmin):
    form = CustomChangeForm
    add_form = CustomCreationForm
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff")
    ordering = ("email",)

    fieldsets = (
        (_("Login info"), {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

admin.site.register(CustomUser, CustomAdmin)