from django.contrib import admin
from .models import UserProfile, Indication

@admin.register(Indication)
class IndicationAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

# Register your models here.
