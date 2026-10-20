from django.db import models

# Create your models here.
from django.db import models

# Feature 1: Master Factory Structure
class MachineTool(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., CNC Lathe #04")
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Maintenance', 'Maintenance')], default='Active')

    def __str__(self):
        return self.name

# Feature 2 & 4: Raw Material Dock Intake & Status for Supervisor
class RawMaterialIntake(models.Model):
    supplier_name = models.CharField(max_length=200)
    po_number = models.CharField(max_length=100, verbose_name="Purchase Order Number")
    material_grade = models.CharField(max_length=100)
    heat_number = models.CharField(max_length=100)
    quantity_received = models.IntegerField()
    
    # This fulfills the supervisor approval/quarantine requirement
    status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Quarantined', 'Quarantined')], 
        default='Pending'
    )
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Heat {self.heat_number} - {self.supplier_name}"

# Feature 3: Digital Shift Handover Logbook
class ShiftHandover(models.Model):
    machine = models.ForeignKey(MachineTool, on_delete=models.CASCADE)
    active_job_status = models.CharField(max_length=200)
    total_parts_produced = models.IntegerField()
    current_scrap_count = models.IntegerField()
    machine_health_notes = models.TextField()
    shift_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Handover: {self.machine.name} - {self.shift_date.strftime('%Y-%m-%d')}"
