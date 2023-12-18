from django.db import models


class User(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=36, primary_key=True)
    password = models.CharField(max_length=60)
    money = model.DecimalField(max_digits = 5, decimal_places= 0)

class UserProduct(models.Model):
    userid = models.CharField(max_length=60)
    productid =  models.CharField(max_length=60)
    description = models.CharField(max_length=10)
    posX = models.DecimalField(max_digits = 4, decimal_places= 0)
    posY = models.DecimalField(max_digits = 4, decimal_places= 0)

class Pet(models.Model):
    userid = models.CharField(max_length=60)
    petid = models.CharField(max_length=60)
    name = models.CharField(max_length=36)
    breed = models.CharField(max_length=10)
    gender = models.TextChoices("Male","Female","Neutral")
    age = models.DecimalField(max_digits = 3, decimal_places= 0)
    weight = model(max_digits = 5, decimal_places= 1)

class Product(models.model):
    productid =  models.CharField(max_length=60)
    name =  models.CharField(max_length=36)
    price = models.DecimalField(max_digits = 5, decimal_places= 0)
    image = models.ImageField(upload_to='uploads/products')
    product_type = models.TextChoices("Hat","Clothes","Background")

class Diary(models.model):
    petid = models.CharField(max_length=60)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='uploads/diary')
    content = models.TextField()
    place = models.CharField(max_length=120)
    mood = models.TextChoices("Happy","Content","Sad")
    weight = models.DecimalField(max_digits = 6, decimal_places= 3) #kg 
    water_intake = models.DecimalField(max_digits = 4, decimal_places= 0) #ml 
    food_intake = models.DecimalField(max_digits = 5, decimal_places= 3) #kg
    defecation = models.TextChoices("Diarrhea","Normal","Constipation")
    abnormality =  models.TextField()
    medical_record =  models.TextField()
