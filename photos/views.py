import photos
from django.http.response import Http404
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def homepage(request):

    title = 'Home'
    images = Image.get_images()
    return render(request, 'all-photos/photos.html',{'title':title, "images":images})


def location(request,id):
    try:
        location = Location.objects.get(id = id)
        images = Image.objects.filter(location = location.id)
    except:
        raise Http404()
    return render(request, 'all-photos/location.html', {'location':location, 'images':images})

    
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_image = request.GET("category")
        searched_images = Image.search_image_category(search_image)
        message = f'{search_image}'

        return render(request, 'all-photos/search.html', {'message':message, "photos":searched_images})
    else:  
        message = 'You have not searched '
        return render(request, 'all-photos/search.html', {'message': message})

