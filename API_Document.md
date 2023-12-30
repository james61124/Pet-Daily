# API
## login page
### /User/Register *POST*
**request**
> 照片還沒處理
username 不能重複
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
header:
{ 
	"content_type" : 'application/json'
}
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
header:
{ 
	"content_type" : 'application/json'
}
```
data:
{
	"userID" : "",
	"petID" : ""
}
```


## dress up page

### /Shop/GetDressPageInfo *POST*

> 這是剛進到 Dress Page 會拿到的所有資料
Dressup Product 就是之前已經著裝過的寵物的衣服位置
Shop Product 就是商店裡的所有商品，先給價格就好，status 還沒處理

**request**
```
header:
{ 
	"content_type" : 'application/json'
}
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
	"date" : “”
}
files : {
    'image': 
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

### /Diary/UploadDiary *POST*
> description: upload diary at the current date
目前 mood, abnormality 沒有擋型態，前端傳甚麼後端就存甚麼
**request**
```
header:
{ 
	"content_type" : 'application/json'
}
data:
{
	"petid" : ,
	"date" : ,
	"content" : ,
	"place" : ,
	"mood" : ,
	"weight" : ,
	"water_intake" : ,
	"food_intake" : ,
	"defecation" : ,
	"abnormality" : ,
	"medical_record" :
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
	"petid" : ,
	"date" : ,
	"content" : ,
	"place" : ,
	"mood" : ,
	"weight" : ,
	"water_intake" : ,
	"food_intake" : ,
	"defecation" : ,
	"abnormality" : ,
	"medical_record" :
}
```

### /Diary/GetDiaryInfo *POST*
> 表示要取得這個日期之前所儲存的資料
目前 iot 接到資料了，但是還沒更新上資料庫
**request**
```
header:
{ 
	"content_type" : 'application/json'
}
data:
{
	"petid" : ,
	"date" : 
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
	"petid" : ,
	"date" : ,
	"image" : ,
	"content" : ,
	"place" : ,
	"mood" : ,
	"weight" : ,
	"water_intake" : ,
	"food_intake" : ,
	"defecation" : ,
	"abnormality" : ,
	"medical_record" :
}
```


## main page

### /Main/GetMainPagePetInfo *POST*
> 還沒處理寵物圖片的部分
**request**
```
header:
{ 
	"content_type" : 'application/json'
}
data:
{
	"petid" : ,
	"date" : 
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
	"money": ,
	"name": ,
	"breed": ,
	"age":
}
```



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
```
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
    date = models.DateTimeField(auto_now=True)
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
```




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

