from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

class PDU(models.Model):
    
    StateChoices = [
        ("In operation","In Operation"),
        ("Unavailable", "Unavailable")
    ]
    
    name = models.CharField(max_length=100)
    
    location = PlainLocationField(based_fields=['city'], zoom=7)
    
    state = models.CharField(choices = StateChoices, default='In operation',max_length=20)
    
    def __str__(self):
        return self.name
 