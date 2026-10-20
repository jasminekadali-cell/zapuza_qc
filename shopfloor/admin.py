from django.contrib import admin
from .models import MachineTool, RawMaterialIntake, ShiftHandover

# This customizes the Supervisor Dashboard to show the status columns
class RawMaterialIntakeAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'material_grade', 'heat_number', 'status')
    list_filter = ('status',)

# Register the models so they appear in the UI
admin.site.register(RawMaterialIntake, RawMaterialIntakeAdmin)
admin.site.register(MachineTool)
admin.site.register(ShiftHandover)