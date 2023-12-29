# Database 
## User
* UserID 		
* Username	
* Password
* Money

## User Product  
* User ID    	//Owner
* Product ID 
* Description		//Dressed? 
* Position 

## Pet
* PetID 
* UserID 	//Owner
* Name
* Breed
* Gender
* Age
* Weight


## Product
* ProductID
* Name
* Price
* Image		
* Product_Type


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
## login page：
### /User/Register *POST*
**request**\
data: \
{\
	“username” : “”\
	“password” : “”\
	"breed" : “”\
	"petName" : “”\
	"age" : “”\
	"gender" : “”\
}
**response**\
data:\
{\
	"userID" : "",
	"petID" : ""
}

### /User/Login *POST*
**request**\
data:\
{\
	“username” : “”\
	“password” : “”\
}\
**response**\


### /Diary/GetDressPageInfo *POST*

**request**\
data:
{
	“userID” : "",
	“petID” " ""
}
**response**\
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

