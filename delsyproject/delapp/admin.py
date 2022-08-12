from django.contrib import admin
from delapp.models import *
# Register your models here.

class ExperianbceAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'fromDate', 'toDate', 'address', 'employee']
admin.site.register(Experience, ExperianbceAdmin)

class AddressDetailsAdmin(admin.ModelAdmin):
    list_display = ['hno', 'street', 'city', 'state', 'employee']
admin.site.register(AddressDetails, AddressDetailsAdmin)

class QualificationAdmin(admin.ModelAdmin):
    list_display = ['qualificationName', 'percentage', 'employee']
admin.site.register(Qualification, QualificationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'employee']
admin.site.register(Project,ProjectAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'gender', 'phoneNo', 'photo']
admin.site.register(Employee, EmployeeAdmin)