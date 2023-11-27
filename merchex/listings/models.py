from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    #description = models.fields.CharField(max_length=1000)
    #sold = models.fields.BooleanField(default=False)
    #year = models.fields.IntegerField(
    #    validators=[MinValueValidator(1900), MaxValueValidator(2023)],
    #    null=True)
    

    # definition de l'affichage dns l'administration
    def __str__(self):
        return f'{self.name}'
    


class Listing(models.Model):

    class Type(models.TextChoices):
        Records = 'Disques'
        Clothing = 'Vetements'
        Posters = 'Affiches'
        Miscellaneous = 'Divers'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)],
        null=True
    )
    type = models.fields.CharField(choices=Type.choices, max_length=20)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    # definition de l'afichage dans l'administration
    def __str__(self):
        return f'{self.title}'