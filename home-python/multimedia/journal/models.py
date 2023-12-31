from django.db import models
import uuid


class User(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=60)
    money = models.DecimalField(max_digits = 5, decimal_places= 0, default=1000)

class UserProduct(models.Model):
    userid = models.CharField(max_length=60)
    productid = models.CharField(max_length=60)
    description = models.CharField(max_length=10)
    posX = models.DecimalField(max_digits = 4, decimal_places= 0)
    posY = models.DecimalField(max_digits = 4, decimal_places= 0)
    width = models.DecimalField(max_digits = 4, decimal_places= 0, default=0)
    height = models.DecimalField(max_digits = 4, decimal_places= 0, default=0)
    zIndex = models.DecimalField(max_digits = 4, decimal_places= 0, default=0)
    equipped = models.DecimalField(max_digits = 4, decimal_places= 0, default=0)

class Pet(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'
        NEUTRAL = 'Neutral', 'Neutral'
    userid = models.CharField(max_length=60)
    petid = models.CharField(max_length=60)
    name = models.CharField(max_length=36)
    breed = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    age = models.DecimalField(max_digits = 3, decimal_places= 0)
    weight = models.DecimalField(max_digits = 5, decimal_places= 1)

class Product(models.Model):
    class ProductType(models.TextChoices):
        HAT = 'Hat', 'Hat'
        CLOTHES = 'Clothes', 'Clothes'
        BACKGROUND = 'Background', 'Background'
    productid =  models.CharField(max_length=60)
    name =  models.CharField(max_length=36)
    price = models.DecimalField(max_digits = 5, decimal_places= 0)
    image = models.CharField(max_length=100)
    product_type = models.CharField(max_length=10, choices=ProductType.choices)
    

class Diary(models.Model):
    class Mood(models.TextChoices):
        HAPPY = 'Happy', 'Happy'
        CONTENT = 'Content', 'Content'
        SAD = 'Sad', 'Sad'
    class Defecation(models.TextChoices):
        DIARRHEA = 'Diarrhea', 'Diarrhea'
        NORMAL = 'Normal', 'Normal'
        CONSTIPATION = 'Constipation', 'Constipation'
    petid = models.CharField(max_length=60)
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=100)
    content = models.TextField()
    place = models.CharField(max_length=120)
    mood = models.CharField(max_length=10, choices=Mood.choices)
    weight = models.DecimalField(max_digits = 6, decimal_places= 3) #kg 
    water_intake = models.DecimalField(max_digits = 4, decimal_places= 0) #ml 
    food_intake = models.DecimalField(max_digits = 5, decimal_places= 3) #kg
    defecation = models.CharField(max_length=20, choices=Defecation.choices)
    abnormality =  models.TextField()
    medical_record =  models.TextField()

class IotWeight(models.Model):
    date = models.DateTimeField(auto_now=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)  # kg 

class IotWaterIntake(models.Model):
    date = models.DateTimeField(auto_now=True)
    water_intake = models.DecimalField(max_digits=4, decimal_places=0)  # ml 

class IotFoodIntake(models.Model):
    date = models.DateTimeField(auto_now=True)
    food_intake = models.DecimalField(max_digits=5, decimal_places=3)  # kg