from django.db import models

# Create your models here.

class Document(models.Model):
   
    document = models.FileField(upload_to='documents/')
    documnet_number=models.CharField(max_length=10 ,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


   