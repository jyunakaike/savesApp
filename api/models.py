from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AMOptions(models.Model):
    name = models.CharField(max_length=200)

class AccountMovement(models.Model):
    Amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    detail = models.TextField()
    # date = models.DateField(null=False, blank=False)
    date = models.DateField(auto_now_add= True)
    created_at=models.DateField(auto_now_add= True)
    updated_at =models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to= User, on_delete=models.CASCADE)
    options = models.ForeignKey(to= AMOptions, on_delete=models.CASCADE, default=1 )
    # type = 
    class Meta:
        ordering: ['updated_at']

    def __str__(self):
        return str(self.owner)+'s Account Movement'
