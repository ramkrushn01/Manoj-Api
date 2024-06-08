from django.db import models
import json 

class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colors = models.CharField(max_length=1000)  # Store colors as JSON string
    image = models.ImageField(upload_to='product_images/',default='')
    description = models.TextField()
    category = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)

    @property
    def color(self):
        return json.loads(self.colors)

    @color.setter
    def color(self, value):
        self.colors = json.dumps(value)

class Images(models.Model):
    id = models.CharField(max_length=225,primary_key=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    url = models.CharField(max_length=2000,default="")
    filename = models.CharField(max_length=225,default="")
    size = models.IntegerField(default=0)
    type = models.CharField(max_length=225,default="")



class MyProduct(models.Model):
    id = models.CharField(max_length=1224,primary_key=True)
    name = models.CharField(max_length=1224,default="")
    company = models.CharField(max_length=1124,default="")
    price = models.IntegerField(default=0)
    color = models.JSONField(default=dict)
    description = models.TextField()
    category = models.CharField(max_length=225)
    featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    stars = models.FloatField(default=0)
    images = models.ManyToManyField(Images)

