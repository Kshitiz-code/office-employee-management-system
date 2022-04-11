from django.contrib import admin

from .models import Department, Employee, Role

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee)
