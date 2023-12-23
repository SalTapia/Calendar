from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    post_like = models.ManyToManyField(User,blank=True)
    def __str__(self):
      return self.title
    @property
    def get_html_url(self):
        url = reverse('cal:event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    

class CommentModel(models.Model):
  name = models.CharField(max_length=10)
  event = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True,blank=True)  
  description = models.TextField(null=True,max_length=300)
  created = models.DateTimeField(auto_now_add=True,null=True)
  image = models.ImageField(upload_to='images',blank=True,null=True)
  video = models.FileField(upload_to='videos',null=True,blank=True)
  def __str__(self):
      return self.name 