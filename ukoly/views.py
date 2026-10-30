from django.shortcuts import render
from .models import Ukol
from django.shortcuts import render, get_object_or_404

def ukol_list(request):
    ukoly = Ukol.objects.filter(splneno__isnull=True).order_by('termin')
    return render(request, 'ukoly/ukol_list.html', {"ukoly":ukoly})
def ukol_detail(request, pk):
    ukol = get_object_or_404(Ukol, pk=pk)
    return render(request, 'ukoly/ukol_detail.html', {'ukol': ukol})