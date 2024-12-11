from django.db import models

def gerar_rota_Imagem_Produto(Produto_refere):
    return f'static/images/{Produto_refere}/produto'
    


# Create your models here.
class Categoria(models.Model):
    Categoria_produtos = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Categoria_produtos}'


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    quanto_custa = models.DecimalField(max_digits=10, decimal_places=2)
    categoria_produto = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, seu valor é {self.quanto_custa}, a sua categoria é {self.categoria_produto}'



class Imagem_produto(models.Model):
    produto_refere = models.ForeignKey(Produto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=gerar_rota_Imagem_Produto(produto_refere))
    alt = models.CharField(max_length=200)
    
    def __str__(self):
        return f'essa foto é do produto {self.produto_refere} e o texto caso não carregue é {self.alt}'