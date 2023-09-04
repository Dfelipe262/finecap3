from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()
    
    def __str__(self):
        return f"Localizacao: {self.localizacao}"
    
    def __str__(self):
        return f"valor: {self.valor}"

class Reserva(models.Model):
    cnpj = models.CharField(max_length=100)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField(default=False)
    imagem =models.ImageField(default=False, required=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
   




 
    
   