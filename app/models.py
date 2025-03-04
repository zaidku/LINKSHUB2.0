# app/models.py
from django.db import models

class Model3D(models.Model):
    name = models.CharField(max_length=255)  # Name of the 3D model
    file = models.FileField(upload_to='models/')  # Store uploaded 3D models
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp when uploaded


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lab_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)




class Case(models.Model):
    case_number = models.CharField(max_length=20, unique=True, blank=True)  # Custom case ID
    patient_name = models.CharField(max_length=255)
    patient_code = models.CharField(max_length=50)
    dentist_name = models.CharField(max_length=255)
    dentistry_type = models.CharField(max_length=50, choices=[("restoration", "Restoration"), ("orthodontics", "Orthodontics")])
    tooth_numbers = models.JSONField(default=list)  # Stores multiple tooth numbers as a list
    shade_system = models.CharField(max_length=50)
    shade = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.case_number:  # Generate case number if it's empty
            last_case = Case.objects.order_by('-id').first()
            next_id = last_case.id + 1 if last_case else 1
            self.case_number = f"CASE-{next_id:05d}"  # Generates CASE-00001, CASE-00002, etc.
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.case_number} - {self.patient_name}"





