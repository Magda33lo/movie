from django.shortcuts import render
from .models import Movie
def home(request):
	if 'search' in request.GET:
		szukaj=request.GET.get('search')
		return render(request, "widok.html", {'movies': Movie.objects.filter(title=szukaj) })
	return render(request, "widok.html", {'movies': Movie.objects.all() })


