from django.db import models





# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
    
class Nutshell(models.Model):
    heading=models.CharField(max_length=30)
    detail= models.CharField(max_length=400)
    def __str__(self):
        return self.heading
    
    
class Gallery(models.Model):
    picture=models.ImageField()
    
    
# class Past_position(models.Model):
    
    
    