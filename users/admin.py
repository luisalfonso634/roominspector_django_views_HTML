#User Admin Classes
#Django
from re import search
from django.contrib import admin

#Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name', 'last_name', 'email', 'user', 'phone_number', 'website','picture')
    list_display_links = ('pk', 'user')
    list_editable = ('email','phone_number', 'website', 'picture')
    search_fields = ('user__email',
                     'user__first_name',
                     'user__last_name',
                     'phone_number')
                     