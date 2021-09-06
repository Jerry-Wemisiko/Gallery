import photos
from django.http.response import Http404
from django.shortcuts import render
from .models import Image

# Create your views here.
def homepage(request):
    title = 'Home'
    images = Image.objects.get()
    return render(request, 'all-photos/photos.html',{'title':title, "image":images})


def search_results(request):
    if 'photo' in request.GET and request.GET['photos']:
        search_image = request.GET('article')
        searched_images = Image.search_image_category(search_image)
        message = f'search_image'

        return render(request, 'all-photos/search.html', {'message':message, "photos":searched_images})
    else:  
        message = 'You have not searched '
        return render(request, 'all-photos/search.html', {'message': message})

