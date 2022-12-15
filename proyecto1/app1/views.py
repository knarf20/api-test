from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render

def page_not_found_view(request):
    return HttpResponse('<h1>TEST asfknbdsfgahjfsjsadsad</h1>')
    #return render(request, '404.html', status=404)