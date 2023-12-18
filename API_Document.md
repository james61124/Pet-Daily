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
}
**response**\
	data:\
	{\
		“description”  // Create Account success or already have account\
	}

### /User/Login *POST*
**request**\
data:\
{\
	“username” : “”\
	“password” : “”\
}\
response
	data:
	{
“UserID”
	"PetID"
}

/User/AddPet POST
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


shop/dressup：
/Diary/GetDressPageInfo

request
	data:
{
	“User ID”
	“Pet ID”
“Page Type”

}
response 
	data: 
	{
		“DressUp Image” : “”,
“Product” : [{
Name
Price
Image		
}, …]
	
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

