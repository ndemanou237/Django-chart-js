from django.db import models

class Statistiques(models.Model):
    mois = models.CharField(max_length=20, unique=True)
    ventes = models.IntegerField()
    visiteurs = models.IntegerField()
    satisfaction = models.IntegerField()
    categorie = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.mois} - Ventes: {self.ventes}, Visiteurs: {self.visiteurs}, Satisfaction: {self.satisfaction}, Categoris: {self.categorie}"
    
