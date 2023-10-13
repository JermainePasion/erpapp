from django.db import models

class  Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    subject= models.TextField()

    def __str__(self):
        return self.firstname

