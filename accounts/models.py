from django.db import models
from django.conf import settings

class DataQuerySet(models.QuerySet):
    pass

class DataManager(models.Manager):
    def get_queryset(self):
        return DataQuerySet(self.model, using=self.db)

# Create your models here.
class Data(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=2000)

    objects = DataManager()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'