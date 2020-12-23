from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    product_descp=models.CharField(max_length=300)
    publish_date=models.DateField()
    image =models.ImageField(upload_to="shop/images",default="")

class Contact(models.Model):
        contact_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50, default="")
        phone = models.CharField(max_length=50, default="")
        desc = models.CharField(max_length=300, default="")

class Order(models.Model):
        order_id=models.AutoField(primary_key=True)
        itemsJson = models.CharField(max_length=500)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50, default="")
        address = models.CharField(max_length=50, default="")
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50)
        zip_code = models.CharField(max_length=50, default="")
        phone = models.CharField(max_length=50, default="")

class login(models.Model):
        login_id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=50)
        password= models.CharField(max_length=50, default="")
        
class register(models.Model):
        username = models.CharField(max_length=50)
        password1= models.CharField(max_length=50, default="")
        email= models.CharField(max_length=50)

def __str__(self):
        return self.product_name
