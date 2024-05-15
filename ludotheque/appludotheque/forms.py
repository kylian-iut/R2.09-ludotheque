from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class GameForm(ModelForm):
    class Meta:
        model = models.Game
        fields = ['title', 'release_date', 'tags', 'resume', 'plateforme']
        labels = {
            'title': _('Titre'),
            'release_date': _('Date de parution'),
            'tags': _('Tags'),
            'resume': _('Résumé'),
            'plateforme': _('Plateforme'),
        }
        help_texts = {
            'title': _('Entrez le titre du jeu-vidéo'),
            'release_date': _('Entrez la date de parution'),
            'tags': _('Précisez les catégories du jeu'),
            'resume': _('Entrez un résumé pour le jeu'),
            'plateforme': _('Sélectionnez la plateforme du jeu'),
        }
        error_messages = {
            'titre': {
                'max_length': _("Le titre est trop long."),
            }
        }


class PlateformeForm(ModelForm):
    class Meta:
        model = models.Plateforme
        fields = ['name', 'creation_date', 'socity']
        labels = {
            'name': _('Nom'),
            'creation_date': _('Date de création'),
            'socity': _('Entreprise'),
        }
        help_texts = {
            'name': _('Entrez le nom de la plateforme'),
            'creation_date': _('Entrez la date de création'),
            'socity': _('Entrez le nom de l\'entreprise'),
        }
        error_messages = {
            'name': {
                'max_length': _("Le nom de la plateforme est trop long."),
            },
            'socity': {
                'max_length': _("Le nom de l\'entreprise est trop long."),
            },
        }

