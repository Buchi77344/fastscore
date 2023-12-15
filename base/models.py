from django.db import models
from django.urls import reverse
from datetime import datetime




class Category(models.Model):
    name= models.CharField(max_length=1223, db_index=True)
    slug = models.SlugField(max_length=244, unique=True)
    
    def get_abdolute_url(self):
        return reverse ('post_list', args=[self.slug])
    def __str__(self):
        return self.name

STATUS = (
    (0,'Draft'),
    (1,'publish')
)

class Post(models.Model):
    category =models.ForeignKey(Category,related_name='post',on_delete=models.CASCADE)
    created_by = models.CharField(max_length=123)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=12, default='admin')
    image =models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=123,unique=True )
    created_on =models.DateTimeField(default=datetime.now, blank=True)
    content  = models.TextField()
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
   
    def get_absolute_url (self):
        return reverse('post_de',args=[self.slug])
    def __str__(self):
       return self.title 

class Comment_Box (models.Model):
    name = models.CharField(max_length=123,  unique=True)
    email = models.EmailField()
    content = models.TextField()
    
class Blink(models.Model):
    user =  models.CharField(max_length=123)
    content= models.TextField()

        


# Create your models here.
