from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    class Meta :
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return str(self.name)
class Item(models.Model):
    name =models.CharField(max_length=255, blank=False,null=True)
    type = models.CharField(max_length=255, blank=True)
    is_sold = models.BooleanField(default=False)
    price = models.FloatField()
    #category = models.ManyToManyField(Category,related_name='items',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='item_photos')
    category = models.ForeignKey(Category,related_name = 'items', on_delete =models.CASCADE,default=None)
    created_by = models.ForeignKey(User,related_name = 'items',on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return str(self.name) + ' ' +str(self.price) 
