from django.contrib import admin
from .models import *
from .models import Post
# Register your models here.



admin.site.register((Appointment,Specialization))
admin.site.register((Post))