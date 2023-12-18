from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from rest_framework_jwt.settings import api_settings
from .models import User, UserProduct, Pet, Product, Diary # add more data
from django.db import connection

import base64 
import io 



### Login Page ### 

def submit(request):
    if request.method == 'GET':

        # check if JWT is correct ( temporaily skip )
        # response = obtain_jwt_token(request)
        # if response.status_code == 200:
        #     return HttpResponse("Submit successful!")
        # else:
        #     return HttpResponseBadRequest("token failed !")
        
        return HttpResponse("Submit successful!")
    else:
        return HttpResponseBadRequest()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user exsits or password is incorrect
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM User WHERE username = %s AND password = %s", [username, password])
            user_data = cursor.fetchone()

        if user_data:
            return HttpResponse("Login successful!")
        else:
            return HttpResponseBadRequest("Username or password is incorrect.")
    else:
        return HttpResponseBadRequest()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if username exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM User WHERE username = %s", [username])
            username_exists = cursor.fetchone()[0]

        if username_exists > 0:
            return HttpResponse("Username already exists!")

        # check password is null
        if not password:
            return HttpResponseBadRequest("Password is null!")

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO User (username, password) VALUES (%s, %s)", [username, password])

        # generate JWT token ( temporaily skip )

        # data = {'username': username}
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(data)
        # token = jwt_encode_handler(payload)

        token = username
        return HttpResponse(f"Register successful! JWT Token: {token}")
    else:
        return HttpResponseBadRequest()

def get_all_user(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT username, password FROM User")
            users = cursor.fetchall()

        user_credentials = [(username, password) for username, password in users]
        return HttpResponse(f"All the users: {user_credentials}")
    else:
        return HttpResponseBadRequest("Invalid request method")

def delete_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        with connection.cursor() as cursor:

            # Check if the user exists before deleting
            cursor.execute("SELECT * FROM User WHERE username = %s", [username])
            user_exists = cursor.fetchone()

            if user_exists:
                cursor.execute("DELETE FROM User WHERE username = %s", [username])
                return HttpResponse(f"User '{username}' deleted successfully.")
            else:
                return HttpResponseBadRequest(f"User '{username}' not found.")
    else:
        return HttpResponseBadRequest("Invalid request method")



# add a new pet for a user
def add_pet(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        breed = request.POST.get('breed')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image_b64 = request.POST.get('image')
        weight = request.POST.get('weight')

        # Convert the base64-encoded image to a binary format
        image_bytes = base64.b64decode(image_b64)
        image = io.BytesIO(image_bytes)

        # insert a new record into Pet table
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Pet (userid, breed, name, age, gender, image, weight) VALUES (%s, %s, %s, %s, %s, %s)",[userid, breed, name, age, gender, image, weight]) 
            pet_id = cursor.lastrowid

        # return the pet id as a response
        return HttpResponse(pet_id)
    else:
        return HttpResponseBadRequest()

# add a photo for a diary entry
def add_photo(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        image_b64 = request.POST.get('image')

        #convert the base64-encoded image into a binary format
        image_bytes = base64.b64decode(image_b64)
        image = io.BytesIO(image_bytes)

        # update the image field of the Diary table
        with connection.cursor() as cursor:
            cursor.execute("UPDATE Diary SET image = %s WHERE date = %s", [image, date])

        # return a success message as a response
        return HttpResponse("Photo added successfully!")
    else:
        return HttpResponseBadRequest()



### NEED CHECK AGAIN ###  

# get the history of a pet's diary entries
def get_history(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        pet_id = request.POST.get('pet_id')
        date = request.POST.get('date')

        # query the Diary table for the matching records
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Diary WHERE PetID = %s AND date = %s", [pet_id, date])
            diary_data = cursor.fetchall()

        # convert the query result into a JSON format
        diary_json = json.dumps(diary_data)

        # return the JSON data as a response
        return HttpResponse(diary_json)
    else:
        return HttpResponseBadRequest()



#get the pet information for a user
def get_pet_info(request): 
    if request.method == "POST": 
        userid = request.POST.get("userid") 
        petid = request.POST.get("petid")

    # check if the user and pet exist
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM User WHERE userid = %s", [userid])
        user_exists = cursor.fetchone()
        cursor.execute("SELECT * FROM Pet WHERE petid = %s", [petid])
        pet_exists = cursor.fetchone()

    if user_exists and pet_exists:
        # get the pet name, type, age, dressup image and selfie
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, breed, age FROM Pet WHERE petid = %s", [petid])
            name,breed,age = cursor.fetchone() 
            cursor.execute("SELECT image FROM UserProduct WHERE userid = %s AND petid = %s AND description = 'Dressed'", [userid, petid])
            dressup_image = cursor.fetchone()[0]
            cursor.execute("SELECT image FROM Diary WHERE petid = %s AND content = 'Selfie'", [petid])
            pet_selfie = cursor.fetchone()[0]

        # return the pet information as a JSON object
        pet_info = {
            'petname': pet_name,
            'pettype': pet_type,
            'petage': pet_age,
            'dressupimage': dressup_image,
            'petselfie': pet_selfie
        }
        return HttpResponse(json.dumps(pet_info))
    else:
        return HttpResponseBadRequest("User or pet not found.")
else:
    return HttpResponseBadRequest("Invalid request method")

# get the user information for a user
def get_user_info(request): if request.method == "POST": userid = request.POST.get("userid")
    # check if the user exists
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM User WHERE userid = %s", [userid])
        user_exists = cursor.fetchone()

    if user_exists:
        # get the user money
        with connection.cursor() as cursor:
            cursor.execute("SELECT money FROM User WHERE userid = %s", [userid])
            user_money = cursor.fetchone()[0]

        # return the user information as a JSON object
        user_info = {
            'money': user_money
        }
        return HttpResponse(json.dumps(user_info))
    else:
        return HttpResponseBadRequest("User not found.")
else:
    return HttpResponseBadRequest("Invalid request method")

# get the history information for a user and a pet
def get_history_info(request): if request.method == "POST": userid = request.POST.get("userid") petid = request.POST.get("petid")

    # check if the user and pet exist
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM User WHERE userid = %s", [userid])
        user_exists = cursor.fetchone()
        cursor.execute("SELECT * FROM Pet WHERE petid = %s", [petid])
        pet_exists = cursor.fetchone()

    if user_exists and pet_exists:
        # get the dates of all the diary entries for the pet
        with connection.cursor() as cursor:
            cursor.execute("SELECT date FROM Diary WHERE petid = %s", [petid])
            dates = cursor.fetchall()

        # return the history information as a JSON object
        history_info = {
            'dates': [date[0] for date in dates]
        }
        return HttpResponse(json.dumps(history_info))
    else:
        return HttpResponseBadRequest("User or pet not found.")
else:
    return HttpResponseBadRequest("Invalid request method")