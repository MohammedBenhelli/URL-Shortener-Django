from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import URL

def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.click()
    return redirect(url.url)

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'urls': URL.objects.all()}, request))

def post(request):
    print(request.POST.get('link'))
    url = URL(url=request.POST.get('link'))
    url.save()
    return redirect('/')
