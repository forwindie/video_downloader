from django.shortcuts import render, redirect
from convapp.models import Query
from convapp.forms import QueryForm
import youtube_dl


def index(request):
    links = Query.objects.all()

    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid:
            link = request.POST['link']
            form.save()
            return redirect(link)
    else:
        form = QueryForm()

    return render(request, 'index.html', {'links': links, 'form': form})


def download():
    pass
