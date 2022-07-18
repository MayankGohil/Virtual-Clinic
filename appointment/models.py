from django.db import models
from account.views import Doctor,Patient
# Create your models here.


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    time = models.DateTimeField(null=True,blank=True)
    fees_paid = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    link = models.URLField(max_length=200,null=True,blank=False)

class Specialization(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/specialization',null=True,blank=True)

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    img =models.ImageField(upload_to='images/blogs',null=True,blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author
