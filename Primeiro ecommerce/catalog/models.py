from django.db import models
from django.urls import reverse


class Category(models.Model):
    
    name = models.CharField("Nome",max_length=100)
    slug = models.SlugField("Identificador",max_length=100)

    created = models.DateTimeField("Criado em",auto_now_add=True) #DATA ATUAL
    modified = models.DateTimeField("Modificado em",auto_now=True) #data atual quando foi salvo

    class Meta:
        verbose_name =  "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category", kwargs={"category_slug": self.slug})
    
class Product(models.Model):
    name = models.CharField("Nome",max_length=100)
    slug = models.SlugField("Identificador",max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    description = models.TextField("Descrição",blank=True)
    price =  models.DecimalField("Preço",decimal_places=2,max_digits=8)#decimal bem definido

    created = models.DateTimeField("Criado em",auto_now_add=True) #DATA ATUAL
    modified = models.DateTimeField("Modificado em",auto_now=True) #data atual quando foi salvo

    class Meta:
        verbose_name =  "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]
    
    def __str__(self):
        return self.name



