from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes preférés sont :</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons Merch !</p>')

def listings(request):
    lisitings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings</h1>
        <p>C\'est la page Listings.</p>
        <ul>
            <li>{lisitings[0].title}</li>
            <li>{lisitings[1].title}</li>
            <li>{lisitings[2].title}</li>
        </ul>
    """)

def contact(request):
    return HttpResponse('<h1>Contactez-nous !</h1> <p>Vous êtes sur la page de contac !</p>')