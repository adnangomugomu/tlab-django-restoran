from django.db import models
from django.utils import timezone
from resep.models import Resep
    
class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted__isnull=True)

class Bahan(models.Model):
    komponen = models.CharField(max_length=255,null=True,blank=True)
    resep = models.ForeignKey(Resep,on_delete=models.DO_NOTHING,null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)    
    deleted = models.DateTimeField(null=True)    

    objects = ModelManager()

    def __str__(self):
        return self.komponen

    def soft_delete(self):
        self.deleted = timezone.now()
        self.save()

    class Meta:
        db_table="bahan"