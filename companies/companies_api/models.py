from uuid import uuid4
from django.db import models
    

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
