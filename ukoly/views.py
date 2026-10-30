from django.shortcuts import render
from .models import Ukol

def ukol_list(request):
    ukoly = Ukol.objects.filter(splneno__isnull=True).order_by('termin')
    return render(request, 'ukoly/ukol_list.html', {"ukoly":ukoly})