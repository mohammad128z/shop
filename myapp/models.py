from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')
    
    def __str__(self):
        return self.name



@receiver(pre_delete, sender=products)
def mymodel_delete(sender, instance, **kwargs):
    # Delete the file from the filesystem
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)