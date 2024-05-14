from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timezone
from .mangers import UserManager
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError


# Create your models here.

email_regex = RegexValidator(
    regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', message="Please enter valid Email address.")
string_regex = RegexValidator(regex=r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$',
                              message="Some special characters like (~!#^`'$|{}<>*) are not allowed.")
mobile_validate = RegexValidator(
    regex=r'^(\+\d{1,3})?\d{10}$', message='Enter a valid 10-digit mobile number +91 9999999999')


class DateTimes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class User(AbstractUser):

    username = None
    email = models.EmailField(
        unique=True, db_index=True, validators=[email_regex])
    first_name = models.CharField(
        max_length=50, blank=True, null=True, validators=[string_regex])
    last_name = models.CharField(
        max_length=50, blank=True, null=True, validators=[string_regex])
    phone_number = models.CharField(
        max_length=10, blank=True, null=True, validators=[mobile_validate])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    zipcode = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(default=str(datetime.now()))

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.email)+"--"+str(self.first_name)

    # def save(self, *args, **kwargs):

    #     super().save(*args, **kwargs)


class IncidentDetails(DateTimes):
    PRIORITY_CHOICES = (
        ("High", "High"),
        ('Medium', "Medium"),
        ("Low", "Low"),
    )
    INCIDENT_STATUS_CHOICES = (
        ("Open", "Open"),
        ('In-Progress', "In-Progress"),
        ("Resolve", "Resolve"),
    )

    incident_number = models.CharField(
        max_length=15,  blank=False, null=False, unique=True)
    reporter_name = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    incident_details = models.TextField()
    reported_datetime = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    incident_status = models.CharField(
        max_length=20, choices=INCIDENT_STATUS_CHOICES, default='Open')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.incident_number)+'--'+(self.priority)
