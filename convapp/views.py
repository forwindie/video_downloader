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
            with youtube_dl.YoutubeDL({'format': '134'}) as ydl:
                result = ydl.extract_info(link, download=False)
                video_url = result['url']
            form.save()
            return redirect(video_url)
    else:
        form = QueryForm()

    return render(request, 'index.html', {'links': links, 'form': form})


