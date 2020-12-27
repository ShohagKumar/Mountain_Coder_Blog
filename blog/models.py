from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    desc = models.TextField()

    def __str__(self):
        return self.name
    objects = models.Manager()
