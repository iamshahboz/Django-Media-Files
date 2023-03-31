from django.db import models
from .validators import validate_string

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=69, validators=[validate_string])
    image = models.ImageField(upload_to='dogs/')

# this method will allow you to delete the file from media root, while delete method called
    def delete(self):
        self.image.delete()
        super().delete()


