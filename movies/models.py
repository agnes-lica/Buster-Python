from django.db import models


class Movie(models.Model):
    FILM_CLASSIFICATION_CHOICES = (("G", "G"), ("PG", "PG"), ("PG-13", "PG-13"), ("R", "R"), ("NC-17", "NC-17"))
    
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(max_length=20, choices=FILM_CLASSIFICATION_CHOICES, default=FILM_CLASSIFICATION_CHOICES[0][1])
    synopsis = models.TextField(null=True)
    added_by=models.EmailField()
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")