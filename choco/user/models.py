from django.db import models
from app.models import chocolate

# Create your models here.
class bookingform(models.Model):
    customer_naame=models.CharField(max_length=50)
    purchase_date=models.DateField()
    title=models.ForeignKey(chocolate,on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
    quantity=models.CharField(max_length=50)
    delivery_address=models.CharField(max_length=100)