from django.urls import path
from . import ludotheque_views, plateformes_views, views

urlpatterns = [
    path('', views.home),
    path('ludotheque/', ludotheque_views.home),
    path('ludotheque/show/<int:id>/', ludotheque_views.show_ludotheque),
    path('ludotheque/add/', ludotheque_views.add_ludotheque),
    path('ludotheque/processing/', ludotheque_views.processing),
    path('ludotheque/update/<int:id>/', ludotheque_views.update_ludotheque),
    path('ludotheque/processing_update/<int:id>/', ludotheque_views.processing_update),
    path('ludotheque/delete/<int:id>/', ludotheque_views.delete_ludotheque),
    path('plateformes/', plateformes_views.home),
    path('plateformes/add/', plateformes_views.add_plateformes),
    path('plateformes/processing/', plateformes_views.processing),
    path('plateformes/show/<int:id>/', plateformes_views.show_plateformes),
    path('plateformes/update/<int:id>/', plateformes_views.update_plateformes),
    path('plateformes/processing_update/<int:id>/', plateformes_views.processing_update),
    path('plateformes/delete/<int:id>/', plateformes_views.delete_plateformes),
]