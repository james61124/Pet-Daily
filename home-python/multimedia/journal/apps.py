from django.apps import AppConfig
from django.db import connection
import os


class JournalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal'

    def ready(self):
        
        directory = "/home/multimedia/journal/image/shop/chinese_new_year"
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                image = "http://107.191.60.115:81/image/shop/chinese_new_year/" + filename
                productid = filename
                name = filename
                price = 10
                product_type = "chinese_new_year"

                # Check if filename already exists in the Product table
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM Product WHERE productid = %s", [productid])
                    count = cursor.fetchone()[0]

                # If the count is 0, the filename does not exist, so insert it
                if count == 0:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO Product (productid, name, price, image, product_type) VALUES (%s, %s, %s, %s, %s)", [productid, name, price, image, product_type])
                
        
        directory = "/home/multimedia/journal/image/shop/christmas"
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                image = "http://107.191.60.115:81/image/shop/christmas/" + filename
                productid = filename
                name = filename
                price = 10
                product_type = "christmas"

                # Check if filename already exists in the Product table
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM Product WHERE productid = %s", [productid])
                    count = cursor.fetchone()[0]

                # If the count is 0, the filename does not exist, so insert it
                if count == 0:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO Product (productid, name, price, image, product_type) VALUES (%s, %s, %s, %s, %s)", [productid, name, price, image, product_type])
            
