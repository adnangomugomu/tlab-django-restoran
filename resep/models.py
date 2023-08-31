from django.db import models
from django.utils import timezone
from kategori.models import Kategori
    
class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted__isnull=True)

class Resep(models.Model):
    makanan = models.CharField(max_length=255,null=True,blank=True)
    kategori = models.ForeignKey(Kategori,on_delete=models.DO_NOTHING,null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)    
    deleted = models.DateTimeField(null=True)    

    objects = ModelManager()

    def __str__(self):
        return self.makanan

    def soft_delete(self):
        self.deleted = timezone.now()
        self.save()

    class Meta:
        db_table="resep"
