from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from rest_framework_jwt.settings import api_settings
from .models import User
from django.db import connection

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
