from django.shortcuts import render
from .models import Statistiques

def dashboard(request):
    stats = Statistiques.objects.all()

    # premier graphique en ligne chart
    line_labels = [s.mois for s in stats]
    line_data = [s.visiteur for s in stats]

    # deuxieme graphique en bar
    bar_labels = [s.mois for s in stats]
    bar_data = [s.ventes for s in stats]

    # troisieme graphique en radar
    radar_labels = ['Satisfaction'] * len(stats)
    radar_data = [s.satisfaction for s in stats]

    # quatrieme graphique pour les donut ou beignet
    categories = {}
    for stat in stats:
        if stat.categorie in categories:
            categories[stat.categorie] += 1
        else:
            categories[stat.categorie] = 1

    donut_labels = list(categories.keys()) 
    donut_data = list(categories.values())

    context = {
        'line_labels': line_labels,
        'line_data': line_data,
        'bar_lables': bar_labels,
        'bar_data': bar_data,
        'radar_labels': radar_labels,
        'radar_data': radar_data,
        'donut_labels': donut_labels,
        'donut_data': donut_data
    }         

    return render(request, 'index.html', context)   
