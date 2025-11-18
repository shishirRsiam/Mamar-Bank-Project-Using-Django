from django.db import models
from django.contrib.auth.models import User
from . import constants


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Address"


class UserBankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    nid_number = models.CharField(max_length=25, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    account_no = models.BigIntegerField(unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=1000.00)
    account_type = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=constants.GENDER, default='Other')


    def __str__(self):
        return f"{self.user.username}'s Bank Account"