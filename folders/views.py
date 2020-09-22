from django.shortcuts import render
from folders.models import Folders


def index(request):
    tree = Folders.objects.all()
    return render(request, "index.html", {'tree': tree})

