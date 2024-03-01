from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email=models.EmailField()

    def __str__(self):
        return f"Visiteur {self.email}"


class Review(models.Model):
    author=models.CharField(max_length=255,default=" ")
    title=models.CharField(max_length=255)
    commentaire=models.TextField(
        default=""
    )
    star=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Partenaire(models.Model):
    title=models.CharField(max_length=255)
    link=models.URLField()
    active=models.BooleanField(default=True)
    img=models.ImageField(upload_to="partenaire_img/")

    def __str__(self):
        return self.title


class Magazine(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    active = models.BooleanField(default=True)
    img = models.ImageField(upload_to="magazine_img/")

    def __str__(self):
        return self.title

class Team(models.Model):
    img=models.ImageField(upload_to="Teams")
    nom=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    description=models.TextField()
    link=models.URLField(default="a.com")


class Compositeur(models.Model):
    img = models.ImageField(upload_to="Teams")
    nom = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField(default="")
    link = models.URLField(default="a.com")
