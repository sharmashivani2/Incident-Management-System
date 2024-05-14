from django.contrib import admin
from incident.models import User, IncidentDetails

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','first_name','last_name','phone_number','zipcode', 'city','country', 'is_staff','is_active',)
    fields = ('email','first_name','last_name','phone_number','password', 'zipcode', 'city','country', 'is_staff','is_active',)
    search_fields = ('email','first_name',)
admin.site.register(User, UserAdmin)

class IncidentDetailsAdmin(admin.ModelAdmin):
    list_display = ('id',"incident_number",'reporter_name','incident_details','priority','incident_status',)
    fields = ("incident_number",'reporter_name','incident_details','reported_datetime','priority','incident_status',)
    search_fields = ('incident_number','incident_status',)
admin.site.register(IncidentDetails, IncidentDetailsAdmin)