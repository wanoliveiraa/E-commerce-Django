

from .models import Category

#obs: não se esquecer de colocar o caminho no settings em TEMPLATES
# esteja disponivel em todos templates
def categories(request):
    return {
        "categories": Category.objects.all()
    }