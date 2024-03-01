from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    content=FroalaField()
    description=models.CharField(max_length=1000,default="")
    active=models.BooleanField(default=True)
    type=models.CharField(max_length=200,default="Tutoriel")
    author=models.CharField(max_length=200,default="Anonyme")
    date=models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
