from django.contrib import admin

from .models import HP_User

# Register your models here.
@admin.register(HP_User)
class HP_UserAdmin(admin.ModelAdmin):
    pass
