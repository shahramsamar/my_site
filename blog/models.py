from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


from tinymce.models import HTMLField




class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpeg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = HTMLField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_date']
        
    def __str__(self):
        return "{} - {}".format(self.title, self.id)


    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})
    
class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='blog/',default='blog/default.jpeg')
        name = models.CharField(max_length=255)
        email = models.EmailField()
        subject = models.CharField(max_length=255)
        message = models.TextField()
        approved = models.BooleanField(default=False)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
        
        
        class Meta:
            ordering =['created_date']
        
        
        def __str__(self):
             return self.name
         
        def get_absolute_url(self):
            return reverse("blog:single", kwargs={"pk": self.pk})
         