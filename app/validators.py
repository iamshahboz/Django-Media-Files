from django.core.exceptions import ValidationError

#this is for Dog model
def validate_string(value:str):
        if not isinstance(value,str):
            raise ValidationError("Name must be a string")
        if value.isdigit():
              raise ValidationError("Name must not be integer")
        return value