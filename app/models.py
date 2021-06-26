
from django.db import models


class info_db(models.Model):
    email = models.EmailField(max_length = 254)
    qr_code = models.ImageField(upload_to = 'media', null = True, blank = True)
    surname = models.CharField(max_length = 100)
    other = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    regno = models.CharField(max_length = 100)