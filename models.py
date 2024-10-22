from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

class Theater(models.Model):
     name = models.CharField(max_length=200)
     address = models.CharField(max_length=300, null=True, blank=True)
     number_of_halls = models.IntegerField()

class Hall(models.Model):
     name = models.CharField(max_length=100)
     number_of_seats = models.IntegerField()
     theatre = models.ForeignKey (Theater,on_delete=models.CASCADE)

class Actor(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     date_of_birth = models.DateField(null=True, blank=True)

class Play(models.Model):
     title = models.CharField(max_length=200)
     genre = models.CharField(max_length=50)
     duration = models.TimeField()
     premiere_date = models.DateField()
     director = models.ForeignKey(Director,on_delete=models.SET_NULL, null = True)

class Role(models.Model):
      role_name = models.CharField(max_length=200)
      actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
      play = models.ForeignKey(Play,on_delete=models.CASCADE)

class Buyer(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.CharField(max_length=100, unique=True)

class Seat(models.Model):
     seat_number = models.IntegerField()
     hall = models.ForeignKey(Hall,on_delete=models.CASCADE)

class Schedule(models.Model):
     date = models.DateField()
     time = models.TimeField()
     play = models.ForeignKey(Play,on_delete=models.CASCADE)
     hall = models.ForeignKey(Hall,on_delete=models.CASCADE)

class Ticket(models.Model):
     ticket_number = models.IntegerField(max_length = 50, unique=True)
     seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
     buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
