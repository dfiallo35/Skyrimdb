from django.db import models

class Breed(models.Model):
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.breed
