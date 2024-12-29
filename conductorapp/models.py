from django.db import models

# Create your models here.
class QRModels(models.Model):
     qrcode=models.ImageField(blank=True,upload_to='media/',null=True)
     
class Meta:
        db_table='qrcode_data'