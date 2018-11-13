from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	is_village = models.BooleanField(default=False)
	is_shg = models.BooleanField(default=False)
	
	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "User"

class Village(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    village_name = models.TextField(max_length=50, blank=True)
    raw1 = models.TextField(max_length=50, blank=True)
    raw2 = models.TextField(max_length=50, blank=True)
    raw3 = models.TextField(max_length=50, blank=True)
    labour = models.IntegerField( blank=True)
    water = models.TextField(max_length=1, blank=True)
    landsize = models.BigIntegerField( blank=True)
    contact = models.TextField(max_length=10, blank=True)

class SHG(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shg_name = models.TextField(max_length=100, blank=True)
    fname = models.TextField(max_length=50, blank=True)
    lname = models.TextField(max_length=50, blank=True)
    lat = models.DecimalField(decimal_places=12,max_digits=15,blank=True)
    lon = models.DecimalField(decimal_places=12,max_digits=15,blank=True)
    endproduct = models.TextField(max_length=50, blank=True)
    manpower = models.IntegerField( blank=True)
    contact = models.TextField(max_length=10, blank=True)

class VillageIndustry(models.Model):
	vname = models.TextField(max_length=50, blank=True)
	aerospace = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	agribusiness = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	agriculture = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	air_transport = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	airlines = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	airport_harbour = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	alcoholic_beverages = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	amusement_parks = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	auto_manufacure = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	automobile = models.DecimalField(decimal_places=50,max_digits=55,blank=True)
	automotive = models.DecimalField(decimal_places=50,max_digits=55,blank=True)