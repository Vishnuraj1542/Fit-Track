from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user_details)
admin.site.register(Complaint)
admin.site.register(Feedback)