from django.contrib import admin
# UserAdminをBaseUserAdminとしてimport
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Djangoの言語を変更
# from django.utils.translation import gettext_lazy as _
# Register your models here.
from user.models import User

class UserAdmin(BaseUserAdmin):
    # UserAdminクラスのorderingとlist_display,fieldsetsを使用
    ordering = ["id"]
    list_display = ["email","name"]
    fieldsets = (
        # Titleを記入
        # fieldをusernameからメールアドレスに変更
        ("Api Login", {"fields": ("email", "password")}),
        (
            # _("Permissons"),
            ("Permissons"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            }
        ),
        #(_("Login info"), {"fields": ("last_login",)}),
        (("Login info"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                # fieldをusernameからメールアドレスに変更
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    ),
            },
        ),
    )

# デフォルトのUserAdminクラスではなく、作成したUserAdminクラスを使用
admin.site.register(User,UserAdmin)

