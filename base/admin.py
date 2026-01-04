from django.contrib import admin
from .models import Schedule, BookedSchedule, Slot, Department
from django.contrib.admin import register
# Register your models here.

admin.site.register(Schedule)
admin.site.register(BookedSchedule)
admin.site.register(Slot)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)