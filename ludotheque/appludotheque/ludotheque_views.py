from django.shortcuts import render, HttpResponseRedirect
from .forms import GameForm
from . import models
# Create your views here.


def home(request):
    games = models.Game.objects.all()
    return render(request, 'appludotheque/ludotheque/home.html', {'games': games})


def add_ludotheque(request):
    form = GameForm()
    return render(request, 'appludotheque/ludotheque/add.html', {'form': form})


def processing(request):
    lform = GameForm(request.POST)
    if lform.is_valid():
        lform.save()
        return render(request, 'appludotheque/ludotheque/success.html', {'Game': lform.cleaned_data})
    else:
        return render(request, 'appludotheque/ludotheque/error.html')


def update_ludotheque(request, id):
    Game = models.Game.objects.get(id=id)
    form = GameForm(instance=Game)
    return render(request, 'appludotheque/ludotheque/update.html', {'form': form, 'Game': Game})


def processing_update(request, id):
    lform = GameForm(request.POST)
    if lform.is_valid():
        Game = lform.save(
            commit=False)  # création d'un objet Game avec les données du formulaire mais sans l'enregistrer dans la base.
        Game.id = id  # modification de l'id de l'objet
        Game.save()  # mise à jour dans la base puisque l'id du jeu existe déja.
        return HttpResponseRedirect("/ludotheque/")  # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "appludotheque/ludotheque/update.html", {"form": lform, "id": id})


def show_ludotheque(request, id):
    Game = models.Game.objects.get(id=id)
    return render(request, 'appludotheque/ludotheque/show.html', {'game': Game})


def delete_ludotheque(request, id):
    anime = models.Game.objects.get(id=id)
    anime.delete()
    return HttpResponseRedirect("/ludotheque/")