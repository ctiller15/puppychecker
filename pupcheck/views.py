from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        print("Home page, baby!")
        print(request)
        return HttpResponse(request.POST['file'])
    return render(request, 'home.html')
