# Database 
## User
```
class User(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=60)
    money = models.DecimalField(max_digits = 5, decimal_places= 0, default=1000)
```

## User Product  
```
class UserProduct(models.Model):
    userid = models.CharField(max_length=60)
    productid = models.CharField(max_length=60)
    description = models.CharField(max_length=10)
    posX = models.DecimalField(max_digits = 4, decimal_places= 0)
    posY = models.DecimalField(max_digits = 4, decimal_places= 0)
```

## Pet
```
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
```


## Product
```
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
```


## IotWeight
```
class IotWeight(models.Model):
    date = models.DateTimeField(auto_now=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)  # kg 
```

## IotWaterIntake
```
class IotWaterIntake(models.Model):
    date = models.DateTimeField(auto_now=True)
    water_intake = models.DecimalField(max_digits=4, decimal_places=0)  # ml 
```


## IotFoodIntake
```
class IotWeight(models.Model):
    date = models.DateTimeField(auto_now=True)
    food_intake = models.DecimalField(max_digits=5, decimal_places=3)  # kg
```



## Diary
* PetID
* Date    DATE
* image
* Content
* Place
* Mood
* Weight
* Water-intake
* Food-intake
* Defecation
* Abnormality
* Medical-record


*
# API
## login page
### /User/Register *POST*
**request**
```
header:
{ 
	"content_type" : 'application/json'
}
data:
{
	“username” : “”,
	“password” : “”,
	"breed" : “”,
	"petName" : “”,
	"age" : “”,
	"gender" : “”,
}
```

**response**
```
data:
{
	"userID" : "",
	"petID" : ""
}
```

### /User/Login *POST* 
**request** 
```
header:
{ 
	"content_type" : 'application/json'
}
data:
{
	“username” : “”,
	“password” : “”,
}
```

**response**


## dress up page

### /Shop/GetDressPageInfo *POST*
**request**
header:
{ 
	"content_type" : 'application/json'
}
```
data:
{
	“userID” : "",
	“petID” " ""
}
```
**response**
```
header:
{ 
	"content_type" : 'application/json'
}
```
```
data: 
{
	"money": "",
	"DressUpProduct": [{
		"Image": "",
		"posX": "",
		"posY": ""
	}, ...]
	"ShopProduct": [{
		"price": "",
		"image": ""
	}, ...]
}
```

## diary page

### /Diary/UploadImage *POST*
**request**
```
header:
{ 
	"content_type" : 'multipart/form-data'
}
data:
{
	“userID” : “”,
	“petID” : “”,
	"date" : “”,
	"image" : “”
}
```
**response**
```
header:
{ 
	"content_type" : 'application/json'
}
```
```
data: 
{
	"image": image_url
}
```



## main page




/User/AddPet  POST
request
data:
{
	“breed” : 
	“name” : 
	“age” : 
	“gender” : 
	“image” : 
}
response 
	data:
{
	“petid”
}
diary：
/Diary/AddPhoto POST
request
data:
{
	“date” : 
	“image” : 
}
/Diary/getHistory POST
request
	data:
	{
		"UserID”
		“PetID”
		“date”
}

response
data: 
{
Photo
Content
Place
Mood
Weight
Water-intake
Food-intake
Defecation
Abnormality
Medical-record
} 

homepage：
/Diary/GetPetInfo POST
request 
data:
{
	“UserID"
	“PetID”
}
response 
data:
{
	“PetName”
	“PetType”
	“PetAge”
	“DressUpImage”
	“PetSelfie”
} 

/Diary/Get/UserInfo POST
request 
	data:
	{
		“UserID”
}
response 
data:
{
	“Money”
}

/Diary/Get/HistoryInfo POST
request
	data:
{
	“UserID”
	"PetID"
}
response
	data:
{
	"dates” 	//list of all dates
}













/Diary/Buy POST

request
data:
{
	“User ID”
	“product ID” 
}
response
	data:
	{
		“description”  //Success or Not 
}



/Diary/DressUp POST
request  
data: 
{
“UserID”
	"PetID"
}

response
	data : 
	{
		
}

