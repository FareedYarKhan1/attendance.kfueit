from django.contrib import admin
from .models import attendance
from import_export.admin import ImportExportActionModelAdmin,ExportActionMixin
# Register your models here.




@admin.register(attendance)
class AttendanceAdmin(ExportActionMixin,admin.ModelAdmin):
    date_hierarchy = 'date'