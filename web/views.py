from django.http import HttpResponse
from django.template import loader
from web.models import Farm

def index(request):
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render({}, request))

def map(request):
    template = loader.get_template('web/map.html')
    farms = Farm.objects.all()
    return HttpResponse(template.render({'farms': farms}, request))

def farm_list(request):
    template = loader.get_template('web/farm_list.html')
    farms = Farm.objects.all()
    return HttpResponse(template.render({'farms': farms}, request))