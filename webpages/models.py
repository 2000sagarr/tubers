from django.db import models

# Create your models here.

class Slider(models.Model):
    # charfield is character field
    # we can provide blank = true to charfield if we allowed blank fields. 
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    #for photo handling pillow library is compulsary 
    #upload_to is path to store photo, %Y create year folder
    photo = models.ImageField(upload_to='media/slider/%Y/')
    #DateTimeField -> store current date time
    created_date = models.DateTimeField(auto_now_add= True)
    # url_link = models.CharField(max_length=250)
    #this name will be displayed at admin panel
    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    fb_link = models.CharField(max_length=250)
    linkedIn_link = models.CharField(max_length=250)
    photo = models.ImageField(upload_to = "media/team/%Y/%m/%d/")
    # this is extra added field 
    #so we can pass null =Trur or while migration we can provide
    #default value for this filed
    youtube = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.first_name
    