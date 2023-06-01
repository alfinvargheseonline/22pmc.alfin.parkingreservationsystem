from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    categoryname = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryname


class User_login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    u_type=models.CharField(max_length=100)

    def __str__(self):
        return self.username
class Vehicle(models.Model):
    parkingnumber = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehiclecompany = models.CharField(max_length=50)
    regno = models.CharField(max_length=10)
    ownername = models.CharField(max_length=50)
    ownercontact = models.CharField(max_length=15)
    pdate = models.DateField(default=timezone.now().date(),null=True)
    intime = models.TimeField(default=timezone.now().time(),null=True)
    outtime = models.TimeField(null=True)
    parkingcharge = models.CharField(max_length=50)
    remark = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    user=models.ForeignKey(User_login,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.parkingnumber



class User_details(models.Model):
    user_id=models.IntegerField()
    email=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Parkings(models.Model):
    parking_id = models.IntegerField()
    location = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    park_name = models.CharField(max_length=100)
    slot = models.IntegerField()
    remaining_slot = models.IntegerField(default=0)
    attendant = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.location

class Slots(models.Model):
    slot_no = models.CharField(max_length=100)
    parking = models.ForeignKey(Parkings, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Get the current count of slots associated with the parking
        current_slots_count = Slots.objects.filter(parking=self.parking).count()

        if current_slots_count >= self.parking.slot:
            # Raise an exception or handle the error when the maximum slot count is reached
            raise ValueError("Maximum slot count reached for this parking")

        # Calculate the remaining slots
   

        super().save(*args, **kwargs)

<<<<<<< HEAD
    def __str__(self):
        return self.parking

=======
>>>>>>> dcdd51991e6451e5b7086f8a13edce25391b62fd
class Booking(models.Model):
    user=models.ForeignKey(User_login,on_delete=models.CASCADE)
    slot=models.ForeignKey(Slots,on_delete=models.CASCADE)
    intiime=models.DateTimeField()
<<<<<<< HEAD
    outtime=models.DateTimeField(default=timezone.now)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50)
    parkingcharge=models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.user
=======
    outtime=models.DateTimeField(null=True)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)

    
    status=models.CharField(max_length=50)

>>>>>>> dcdd51991e6451e5b7086f8a13edce25391b62fd


