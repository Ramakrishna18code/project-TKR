from django.contrib import admin
from .models import ClientRegister_Model, content_detection_type

# Register your models here.
admin.site.register(ClientRegister_Model)
admin.site.register(content_detection_type)
