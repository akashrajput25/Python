from django.db import models

# Makemigrations is going here to create database changes and store it in a file.
# Migrate is used to aplly the makemigrations file for our database.

class Contact(models.Model):
    firstname = models.CharField(max_length = 60)
    lastname = models.CharField(max_length = 60)
    email = models.CharField(max_length = 80)
    def __str__(self):
        return self.firstname+" "+self.lastname