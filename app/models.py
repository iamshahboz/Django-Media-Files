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

# Models does not have link in between, it is just for demonstrating django filter
class Book(models.Model):
    class GenreChoices(models.TextChoices):
        CRIME = 'C'
        NON_FICTION = 'N'
        OTHER = 'O'
        SCI_FI = 'S'
    
    name = models.CharField(max_length=128)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=1,choices=GenreChoices.choices)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=128)



