from django.db import models
from django.utils import timezone
    
class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted__isnull=True)

class Kategori(models.Model):
    nama = models.CharField(max_length=255,null=True,blank=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)    
    deleted = models.DateTimeField(null=True)    

    objects = ModelManager()

    def __str__(self):
        return self.nama

    def soft_delete(self):
        self.deleted = timezone.now()
        self.save()

    class Meta:
        db_table="ref_kategori"