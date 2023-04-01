from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import magic 

#this is for Dog model
def validate_string(value:str):
        if not isinstance(value,str):
            raise ValidationError("Name must be a string")
        if value.isdigit():
              raise ValidationError("Name must not be integer")
        return value

ext_validator = FileExtensionValidator(['png','jpg','pdf'])

def validate_file_mimetype(file):
    accept = ['image/png','image/jpeg','application/pdf']
    file_mime_type = magic.from_buffer(file.read(1024),mime=True)
    if file_mime_type not in accept:
        raise ValidationError('unsupported file type')
    
