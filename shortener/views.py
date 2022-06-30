from django.shortcuts import render
from .models import ShortUrl
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        url = data['url']

        shorturl = ShortUrl.objects.create(name=name, url=url)
        print("Short URL created")

    context = {}
    template = "polls/index.html"
    return render(request, template, context)

def rerouter(request, slug):
    url = ShortUrl.objects.get(slug=slug)

    return redirect(url.url)