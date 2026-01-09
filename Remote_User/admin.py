from django.contrib import admin
from .models import ClientRegister_Model, content_detection_type, detection_accuracy, detection_ratio

# Register your models here.
admin.site.register(ClientRegister_Model)
admin.site.register(content_detection_type)
admin.site.register(detection_accuracy)
admin.site.register(detection_ratio)
