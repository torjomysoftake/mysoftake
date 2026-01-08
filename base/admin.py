from django.contrib import admin
from .models import Schedule, BookedSchedule, Slot, Department, UserInformation
from django.contrib.admin import register
# Register your models here.

admin.site.register(Schedule)
admin.site.register(Slot)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)

@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('pk','name','phone_number','email','address','purpose',)

@admin.register(BookedSchedule)
class BookedScheduleAdmin(admin.ModelAdmin):
    list_display = ('user','schedule_date','schedule_slot',)


