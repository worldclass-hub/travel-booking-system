from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Tour

def tour_list(request):
    tours = Tour.objects.all()  # Fetch all tour packages from the database
    return render(request, 'tours/tour_list.html', {'tours': tours})



from django.shortcuts import render, get_object_or_404
from .models import Tour

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)  # Get tour or return 404 if not found
    return render(request, 'tours/tour_detail.html', {'tour': tour})
