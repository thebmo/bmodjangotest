from django.db import models

# Create your models here.
# class user_info(models.Model):
    # username = models.Charfield
class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    email_address = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=500)
    date_joined = models.DateTimeField(blank=True, null=True)
    currently_playing = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'users'

class Games(models.Model):
    gid = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=100)
    genre = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    na_release = models.CharField(max_length=100, blank=True)
    eu_release = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    rating = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'games'


# stupid test stuff for posting        
class TestEntries(models.Model):
    tid = models.IntegerField(primary_key=True)
    test_str = models.TextField()
    class Meta:
        managed = False
        db_table = 'test_entries'
