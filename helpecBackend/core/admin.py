from django.contrib import admin

from .models import HP_User, Contact, Occurrence

# Register your models here.
@admin.register(HP_User)
class HP_UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    pass


@admin.register(Occurrence)
class Occurrence(admin.ModelAdmin):
    pass
