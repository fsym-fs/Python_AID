from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    # return render(request,'music_index.html')
    return render(request, 'music/index.html')
    # return HttpResponse('This is music_index')