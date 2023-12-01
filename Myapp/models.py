from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
import select2.models
import select2.fields
# from star_ratings.models import Rating
# Create your models here.



class Category(models.Model):

    name = models.CharField(max_length = 15)
   
    slug = AutoSlugField(populate_from = 'name', unique=True, max_length=100)
    def __str__(self):
        return str(self.name)
    def get_absolut_url(self):
        return reverse('Myapp:category_filter', args={self.slug})
    

class Product(models.Model):
    
    name = models.CharField(max_length=25) 
    image = models.ImageField(upload_to='products/') 
    slide1 = models.ImageField(upload_to='products/')
    slide2 =  models.ImageField(upload_to='products/')
    slide3 = models.ImageField(upload_to='products/')
    slide4 = models.ImageField(upload_to='products/')
    ingredient1 = models.CharField(max_length=255)
    ingredient2 = models.CharField(max_length=255)

    slug = AutoSlugField(populate_from = 'name', unique=True, max_length=100)
    price = models.FloatField()
    choice = select2.fields.ForeignKey(Category,overlay="Choose a Category...",
        on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    
    def get_absolut_url(self):
        return reverse('Myapp:product_detail', args={self.slug, })

class Feedback(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    feedback  = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    rating = models.PositiveSmallIntegerField(choices=(
        (1, "⭐☆☆☆☆"),
        (2, "⭐⭐☆☆☆"),
        (3, "⭐⭐⭐☆☆"),
        (4, "⭐⭐⭐⭐☆"),
        (5, "⭐⭐⭐⭐⭐"),
    ))

