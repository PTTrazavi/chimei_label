from django.db import models
from django.urls import reverse

class Patient(models.Model):
    name = models.CharField(max_length=64,null=True)
    ref = models.ImageField(upload_to='images/')
    ap = models.ImageField(upload_to='images/')
    apl = models.CharField(max_length=4,null=True)
    lat = models.ImageField(upload_to='images/')
    latl = models.CharField(max_length=4,null=True)
    date_of_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])
