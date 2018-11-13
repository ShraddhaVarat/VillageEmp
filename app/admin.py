from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User, Village,SHG
# Register your models here.
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_village','is_shg',)}),
    )

    list_display = ['username','is_village','is_shg']


admin.site.register(User, MyUserAdmin)
admin.site.register(Village)
admin.site.register(SHG)