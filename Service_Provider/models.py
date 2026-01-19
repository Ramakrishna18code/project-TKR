from django.db import models

# Create your models here.

class detection_ratio(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    class Meta:
        db_table = 'detection_ratio'

    def __str__(self):
        return self.names


class detection_accuracy(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    class Meta:
        db_table = 'detection_accuracy'

    def __str__(self):
        return self.names
