

from .models import Category

#obs: não se esquecer de colocar o caminho no settings em TEMPLATES

def categories(request):
    return {
        "categories": Category.objects.all()
    }