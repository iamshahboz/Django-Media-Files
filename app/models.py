from django.db import models
from .validators import validate_string,validate_file_mimetype,ext_validator



# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=69, validators=[validate_string])
    image = models.FileField(upload_to='dogs/',validators=[ext_validator,validate_file_mimetype])

# this method will allow you to delete the file from media root, while delete method called
    def delete(self):
        self.image.delete()
        super().delete()


