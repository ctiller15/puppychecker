from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        print("Home page, baby!")
        test = request.FILES['file']
        print(test.name)
        print(test.size)
        print(test.content_type)

        path = os.getcwd()
        print(path)

        with open(path + '/pupcheck/saved_images/000001.jpg', 'wb+') as destination:
            for chunk in test.chunks():
                destination.write(chunk)

        return HttpResponseRedirect('/')
    return render(request, 'home.html')
