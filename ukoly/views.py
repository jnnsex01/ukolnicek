from django.shortcuts import render

# Create your views here.
def ukol_list(request):
    return render(request, 'ukoly/ukol_list.html',{})