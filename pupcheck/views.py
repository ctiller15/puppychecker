from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from pupcheck.services.image_analysis import puppy_or_dog_analysis as pda

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

        predicted_class = pda.analyze_age(test)

        print(predicted_class)

        return render(request, 'home.html', {'predicted': predicted_class})
    return render(request, 'home.html')
