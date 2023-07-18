from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    miniature = models.ImageField(upload_to='miniatures/')
    contenu = models.TextField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

