from django.db import models
from stand.models import Stand
    
class Reserva(models.Model):
    cnpj = models.CharField(max_length=100)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()
    imagem =models.ImageField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_empresa}"

    
   




 
    
   