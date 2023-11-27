from django.contrib import admin

from listings.models import Band, Listing

# Register your models here.

class BandAdmin(admin.ModelAdmin): 
    list_display = ('name', 'year_formed', 'genre') # liste les champs a afficher dans l'admin

admin.site.register(Band, BandAdmin) # affichage de l'entité Band dans l'administration

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band') # liste des elements a afficher
admin.site.register(Listing, ListingAdmin)
