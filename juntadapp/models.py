from django.db import models

# Create your models here.
class Room(models.Model):
    #id = models.AutoField(primary_key=True)
    titleRoom = models.CharField(max_length=50)
    passwordRoom = models.CharField(max_length=50)
    

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    userSurname = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    userAlias = models.CharField(max_length=50)
    registerDate = models.DateTimeField(auto_now_add=True)
    
    def completeName(self):
        txt = "{0},{1}"
        return txt.format(self.userName, self.userSurname)
    
    
class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    duration = models.DateTimeField()
    members = models.JSONField()
    rol = models.TextField(max_length=50)
    creator = models.ForeignKey("Account", null=False, blank=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


class Costs(models.Model):
    amount = models.FloatField()
    quantity = models.JSONField()
    members = models.JSONField()
    responsible = models.CharField(max_length=50)
    
    def addCost():
        pass
    
    def deleteCost():
        pass
    
    def assignResponsible():
        pass
    
    
class Payment(models.Model):
    id = models.ForeignKey("Account", null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    # Este no se bien cual es 
    # paymentMethod = models.CharField()
    
class Costs_Details():
    
    def uploadDocument():
        pass
    
    def total():
        pass