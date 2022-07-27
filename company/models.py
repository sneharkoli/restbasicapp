from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


custom = RegexValidator(r'^[a-zA-Z]{2}[0-9]{2}[E|N]$', 'Length should be 5 characters, 1st & 2nd characters should be alphabets, 3rd & 4th characters should be numbers,5th character should be E or N')


class Company(models.Model):
    company_name = models.CharField(max_length = 120, validators=[MinLengthValidator(5)], blank=False, null=False, unique=True)
    email_id = models.EmailField(blank=False, null=False, unique=True)
    company_code = models.CharField(max_length=5, unique=True, blank=True, validators=[custom])
    strength = models.PositiveIntegerField(null=True)
    website = models.URLField(max_length=1200, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

