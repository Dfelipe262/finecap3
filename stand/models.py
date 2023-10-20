from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()
    
    def __str__(self):
        return f"Localizacao: {self.localizacao}"
