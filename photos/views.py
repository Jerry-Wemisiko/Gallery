from django.http.response import Http404
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def homepage(request):

    title = 'Home'
    images = Image.get_images()
    return render(request, 'all-photos/photos.html',{'title':title, 'images':images})


def location(request,location):

    images = Image.objects.filter(location = location.id)
    
    return render(request, 'all-photos/location.html', {'location':location, 'images':images})


def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        categories =Category.objects.filter(category__contains=searched)
        
        return render(request, 'all-photos/search.html', {"searched": searched},{"categories": categories})
    else:  
        return render(request, 'all-photos/search.html')

