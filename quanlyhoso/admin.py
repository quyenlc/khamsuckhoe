from django.contrib import admin

# Register your models here.
from .models import Hospital, Employer, Profile

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact')
    list_display_links = ('name',)
    search_fields = ['name', 'address', 'contact']

admin.site.register(Hospital, HospitalAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    list_display_links = ('name',)
    search_fields = ['name', 'address', 'phone']

admin.site.register(Employer, EmployerAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_birth', 'id_card_number', 'action_date', 'hospital', 
                    'employer', 'phone', 'colored_result', 'is_returned', 'deadline')
    list_display_links = ('name',)
    search_fields = ['name', 'phone']
    list_filter = ('employer', 'result', 'is_returned')

admin.site.register(Profile, ProfileAdmin)
