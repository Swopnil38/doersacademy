from django.db import models

# Create your models here.
class intrested_applicant(models.Model):
    applicant_name = models.CharField(max_length=255)
    applicant_phone = models.CharField(max_length=255)
    applicant_email = models.CharField(max_length=255)
    applicant_course = models.CharField(max_length=255)
    applicant_willingness = models.CharField(max_length=255)
    
    class Meta:
        db_table = "intrested_applicant"
        
class emaillist(models.Model):
    email = models.EmailField(max_length=255)
    class Meta:
        db_table = "emaillist" 
