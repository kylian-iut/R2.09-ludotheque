from django.shortcuts import render, HttpResponseRedirect
from .forms import PlateformeForm
from . import models
# Create your views here.


def home(request):
    plateformes = models.Plateforme.objects.all()
    return render(request, 'appludotheque/plateformes/home.html', {'plateformes': plateformes})


def add_plateformes(request):
    form = PlateformeForm()
    return render(request, 'appludotheque/plateformes/add.html', {'form': form})


def processing(request):
    lform = PlateformeForm(request.POST)
    if lform.is_valid():
        plateforme = lform.save()
        return render(request, 'appludotheque/plateformes/success.html', {'plateforme': plateforme})
    else:
        return render(request, 'appludotheque/plateformes/add.html', {'form': lform})


def show_plateformes(request, id):
    plateforme = models.Plateforme.objects.get(id=id)
    return render(request, 'appludotheque/plateformes/show.html', {'plateforme': plateforme})


def update_plateformes(request, id):
    plateforme = models.Plateforme.objects.get(id=id)
    form = PlateformeForm(instance=plateforme)
    return render(request, 'appludotheque/plateformes/update.html', {'form': form, 'plateforme': plateforme})


def processing_update(request, id):
    plateforme = models.Plateforme.objects.get(id=id)
    lform = PlateformeForm(request.POST, instance=plateforme)
    if lform.is_valid():
        plateforme = lform.save()
        return HttpResponseRedirect("/plateformes/")
    else:
        return render(request, 'appludotheque/plateformes/update.html', {'form': lform, 'plateforme': plateforme})


def delete_plateformes(request, id):
    plateformes = models.Plateforme.objects.get(id=id)
    plateformes.delete()
    return HttpResponseRedirect("/plateformes/")

